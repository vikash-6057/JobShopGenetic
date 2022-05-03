# JobShopScheduling

## To run Genetic Algorithm

`python GA.py`

## To run Conventional Algorithms

`python main.py`

A job scheduler to schedule M jobs on N similar machines.
The input contains the following data:

- The Number of machines
  Followed by for each Job:-

1. Job Name
2. Duration: time taken for job completion
3. Priority: priority of the job. P0>P1>P2
4. Deadline: Expiry time after which job should not be run (The clock starts from 0 and deadline is the actual clock time)
5. UserType: Type of user who has initiated the job, Precedence of users Root>Admin>User

There are various scheduling algorithms-

### Shortest Job First - SJF

Shortes job first (SJF), is a scheduling policy that selects the waiting process with the smallest execution time to execute next.
In case of tie choose the job according to the following order-

1. Priority(higher priority job gets scheduled first)

### First Come First Serve -FCFS

Jobs are executed on first come,first serve basis. Take the input as the order of jobs need to be scheduled.

### Fixed Priority Scheduling -FPS

Each process is assigned a priority. Process with highest priority is to be executed first and so on.
In case of tie choose the job according to the following order-

1. User Type
2. Longest Job First

### Earliest Deadline First - EDF

Next job will be searched on the basis of job which is closest to its deadline.
In case of tie, choose the job according to the following order-

1. Priority(higher priority job gets scheduled first)
2. Duration(lesser duration job gets scheduled first)
   In case we cannot schedule a job such that it completes before its deadline then it should be ignored.

You would be given a list of jobs (refer example below for format) and number of threads as input. You
are expected to print the order of jobs scheduled for each algorithm on each thread as output.

##### Example

###### Input

`Machines= 2`

| Job Name | Duration | Priority | Deadline | User Type |
| -------- | -------- | -------- | -------- | --------- |
| J1       | 10       | P0       | 10       | Root      |
| J2       | 20       | P0       | 40       | Admin     |
| J3       | 15       | P2       | 40       | Root      |
| J4       | 30       | P1       | 40       | User      |
| J5       | 10       | P2       | 30       | User      |

###### Output

JOB SCHEDULER

Enter number of machine(s) :2<br />
Select a '.txt' file : job.txt<br />

First Come First Serve :<br />
Machine : 1 - J1 J3 J5<br />
Machine : 2 - J2 J4<br />

Shortest Job First :<br />
Machine : 1 - J1 J3 J4 <br />
Machine : 2 - J5 J2<br />

Fixed Priority Scheduling : <br />
Machine : 1 - J2 J4 J5<br />
Machine : 2 - J1 J3<br />

Earliest Deadline First :<br />
Machine : 1 - J1 J2 <br />
Machine : 2 - J5 J4<br />

`Gantt Chart`

![FCFS](https://github.com/neelam4/JobShopScheduling/blob/main/Output%20Images/Figure_1.png)
![SJF](https://github.com/neelam4/JobShopScheduling/blob/main/Output%20Images/Figure_2.png)
![FPS](https://github.com/neelam4/JobShopScheduling/blob/main/Output%20Images/Figure_3.png)
![EDF](https://github.com/neelam4/JobShopScheduling/blob/main/Output%20Images/Figure_4.png)
