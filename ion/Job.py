class Job:
    def __init__(self, jobName=None, duration=None, priority=None, deadline=None, userType=None):
        self.jobName = jobName
        self.duration = duration
        self.priority = priority
        self.deadline = deadline
        self.userType = userType

    def getJobName(self):
        return self.jobName

    def setJobName(self, jobName):
        self.jobName = jobName

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration

    def getPriority(self):
        return self.priority
        
    def setPriority(self, priority):
        self.priority = priority

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline):
        self.deadline = deadline

    def getUserType(self):
        return self.userType

    def setUserType(self, userType):
        self.userType = userType