class EDF:
    def __init__(self, jobNames:list()=None, deadline=None):
        self.jobNames = jobNames
        self.deadline = deadline

    def getJobNames(self):
        return self.jobNames

    def setJobNames(self, jobNames):
        self.jobNames = jobNames

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline):
        self.deadline = deadline
