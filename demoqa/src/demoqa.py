# A very simple class to hold the PageObject model of demoqa
class demoqaPageObject:

    def __init__(self):
        self.baseUrl = 'http://store.demoqa.com'
        pass
    
    def getSamplePageXpath(self):
        print('Not defined yet')
        return None

    def getCommentFieldXpath(self):
        print('Not defined yet')
        return None

    def getMailFieldXpath(self):
        print('Not defined yet')
        return None

    def getSendCommentXpath(self):
        print('Not defined yet')
        return None

    def isErrorDisplayed(self):
        print('Not defined yet')
        return None

    def isCommentReceived(self):
        print('Not defined yet')
        return None

    def isTitleExpected(self, title):
        return "ONLINE STORE" in title
