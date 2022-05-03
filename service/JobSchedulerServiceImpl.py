from ion import Job, EDF
from functools import cmp_to_key

import matplotlib.pyplot as plt
import random
class JobSchedulerServiceImpl():

    def plot_gantt(self,threadNo:int,machine_thread:dict,f_name:str,job_name_legend:dict):
        # Declaring a figure "gnt"
        fig, gnt = plt.subplots()

        # Setting Y-axis limits
        gnt.set_ylim(0, 60)

        # Setting X-axis limits
        gnt.set_xlim(0, 150)
        gnt.set_xlabel('Time(unit)')
        gnt.set_ylabel('Machine(s)')
        gnt.set_yticks([10,20,30,40,50])
        # Labelling tickes of y-axis
        gnt.set_yticklabels(['1', '2', '3','4','5'])
        # If you want grid on the plot use
        # gnt.grid(True)
        gnt.grid(False)
        for th in range(threadNo):
            no_of_jobs = len(machine_thread[th])
            get_colors = lambda n:list(map(lambda i: "#"+"%06x" %random.randint(0, 0xFFFFFF),range(n)))
            
            gnt.broken_barh(machine_thread[th],(10*th+6,8),facecolors=get_colors(no_of_jobs))
            width = 0
            for name in range(len(job_name_legend[th])):
                width = machine_thread[th][name][0]
                gnt.annotate(str(job_name_legend[th][name]),xy=(width+3,10*th+9),color='white',fontsize = 16)
                

        plt.title(f_name)
        # plt.legend()
        plt.show()

    
    def assignThreadsToJobs(self, threadNo:int, job:list):

        threads = dict()
        jobNames = list()
        machine_thread = dict()
        job_name_legend = dict()
        thread = 0

        for th in range(threadNo):
            machine_thread[th]=list()
            machine_thread[th].append(tuple((0,0)))
            job_name_legend[th]=list()
        
        for j in job:
            if ((thread % threadNo) not in threads):
                jobNames = list()
                jobNames.append(j.getJobName())
                last_mac = machine_thread[thread%threadNo]
                l = tuple((last_mac[-1][-1]+last_mac[-1][0],j.getDuration()))
                machine_thread[thread%threadNo].append(l)
                job_name_legend[thread%threadNo].append(j.getJobName())
                threads[thread % threadNo] = jobNames
            else:
                jobNames = threads[thread % threadNo]
                jobNames.append(j.getJobName())
                last_mac = machine_thread[thread%threadNo]
                l = tuple((last_mac[-1][-1]+last_mac[-1][0],j.getDuration()))
                machine_thread[thread%threadNo].append(l)
                job_name_legend[thread%threadNo].append(j.getJobName())
            thread += 1

        for th in range(threadNo):
            machine_thread[th].pop(0)
        
        return threads,machine_thread,job_name_legend

    def displayScheduledJobs(self, threads:dict,machine_thread:dict,f_name:str,threadNo:int,job_name_legend:dict):
        for entry in threads:
            print("Machine : {} - ".format(entry+1), end="")
            for name in threads[entry]:
                print(name, end=" ")
            print()

        self.plot_gantt(threadNo,machine_thread,f_name,job_name_legend)

    def shortestJobFirst(self, threadNo:int, job:list):
        print("Shortest Job First : ")
        jobs = job
        f_name = "Shortest Job First"

        def comparator(j1, j2):
            if j1.getDuration() == j2.getDuration():
                return j1.getPriority()-j2.getPriority()
            return j1.getDuration()-j2.getDuration()
        jobs.sort(key=cmp_to_key(comparator))
        threads,machine_thread,job_name_legend = self.assignThreadsToJobs(threadNo, jobs)
        self.displayScheduledJobs(threads,machine_thread,f_name,threadNo,job_name_legend)

    def firstComeFirstServe(self, threadNo:int, job):
        print("First Come First Serve : ")
        jobs = job
        f_name = "First Come First Serve "
        threads,machine_thread,job_name_legend = self.assignThreadsToJobs(threadNo, jobs)
        self.displayScheduledJobs(threads,machine_thread,f_name,threadNo,job_name_legend)

    def fixedPriorityScheduling(self, threadNo:int, job:list):
        print("Fixed Priority Scheduling : ")
        jobs = job
        f_name = "Fixed Priority Scheduling"
        def comparator(j1, j2):
            if j1.getPriority() == j2.getPriority():
                if j1.getUserType() == j2.getUserType():
                    return int(j2.getDuration()-j1.getDuration())
                else:
                    return j1.getUserType()-j2.getUserType()
            return int(j1.getPriority()-j2.getPriority())
        jobs.sort(key=cmp_to_key(comparator))
        threads,machine_thread,job_name_legend = self.assignThreadsToJobs(threadNo, jobs)
        self.displayScheduledJobs(threads,machine_thread,f_name,threadNo,job_name_legend)

    def assignThreadsToJobsForEdf(self, threadNo:int, jobs:list):
        threads = dict()
        edf = EDF.EDF()
        machine_thread = dict()
        thread = 0
        job_name_legend = dict()
        for th in range(threadNo):
            machine_thread[th]=list()
            machine_thread[th].append(tuple((0,0)))
            job_name_legend[th]=list()

        for j in jobs:
            if ((thread % threadNo) not in threads):
                if j.getDuration() <= j.getDeadline():
                    edf = EDF.EDF()
                    edf.setJobNames(list())
                    edf.getJobNames().append(j.getJobName())
                    edf.setDeadline(j.getDuration())
                    threads[thread % threadNo] = edf
                    last_mac = machine_thread[thread%threadNo]
                    l = tuple((last_mac[-1][-1]+last_mac[-1][0],j.getDuration()))
                    machine_thread[thread%threadNo].append(l)
                    job_name_legend[thread%threadNo].append(j.getJobName())
                    thread += 1
            else:
                edf = threads[thread % threadNo]
                if (edf.getDeadline()+j.getDuration() <= j.getDeadline()):
                    edf.setDeadline(edf.getDeadline()+j.getDuration())
                    edf.getJobNames().append(j.getJobName())
                    last_mac = machine_thread[thread%threadNo]
                    l = tuple((last_mac[-1][-1]+last_mac[-1][0],j.getDuration()))
                    machine_thread[thread%threadNo].append(l)
                    job_name_legend[thread%threadNo].append(j.getJobName())
                    thread += 1

        for th in range(threadNo):
            machine_thread[th].pop(0)

        return threads,machine_thread,job_name_legend

    def displayScheduledJobsForEdf(self, threads,machine_thread:dict,f_name:str,threadNo:int,job_name_legend:dict):
        for entry in threads:
            print("Machine : {} - ".format(entry+1), end="")
            for name in threads[entry].getJobNames():
                print(name, end=" ")
            print()
        self.plot_gantt(threadNo,machine_thread,f_name,job_name_legend)

    def earliestDeadlineFirst(self, threadNo:int, job:list):
        print("Earliest Deadline First : ")
        jobs = job
        f_name = "Earliest Deadline First"

        def comparator(j1, j2):
            if j1.getDeadline() == j2.getDeadline():
                if j1.getPriority() == j2.getPriority():
                    return int(j1.getDuration()-j2.getDuration())
                else:
                    return int(j1.getPriority()-j2.getPriority())
            else:
                return int(j1.getDeadline()-j2.getDeadline())
        
        jobs.sort(key=cmp_to_key(comparator))
        threads,machine_thread,job_name_legend = self.assignThreadsToJobsForEdf(threadNo, jobs)
        self.displayScheduledJobsForEdf(threads,machine_thread,f_name,threadNo,job_name_legend)
