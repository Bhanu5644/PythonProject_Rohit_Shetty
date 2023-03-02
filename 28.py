class ChildImpl(Calculator):
    num = 200

    def getCompleteData(self):
        return self.num + self.num + Summation()
