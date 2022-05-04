from ion import Job
from service import JobSchedulerServiceImpl


def main():
    print("JOB SCHEDULER")
    print()
    jobScheduler = JobSchedulerServiceImpl.JobSchedulerServiceImpl()
    job1 = Job.Job("J1", 10, 0, 10, 1)
    job2 = Job.Job("J2", 20, 0, 40, 1)
    job3 = Job.Job("J3", 15, 2, 40, 2)
    job4 = Job.Job("J4", 30, 1, 40, 2)
    job5 = Job.Job("J5", 10, 2, 30, 2)
    job6 = Job.Job("J6", 30, 2, 30, 2)
    jobs = list()
    jobs.append(job1)
    jobs.append(job2)
    jobs.append(job3)
    jobs.append(job4)
    jobs.append(job5)
    jobs.append(job6)
    jobScheduler.firstComeFirstServe(2, jobs)
    print()
    jobScheduler.shortestJobFirst(2, jobs)
    print()
    jobScheduler.fixedPriorityScheduling(2, jobs)
    print()
    jobScheduler.earliestDeadlineFirst(2, jobs)


if __name__ == '__main__':
    main()
