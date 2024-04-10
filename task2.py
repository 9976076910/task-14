import requests

class Users:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    def isConnected(self):
        if self.response.status_code == 200:
            return True
        return False

    def fetchData(self):
        try:
            if self.isConnected():
                return self.response.json()
            raise Exception()
        except:
            print("It is not connected")
            return None
    def getNames(self):
        NameList = []

        if not self.fetchData() is None:
            for userDict in self.fetchData():
                NameList.append(userDict["name"])
            return NameList
        else:
            print("It is not connected")
        for breweries in state["name"]:
             if state == Alaska:
                 print("breweries")
             else:
                 print("none")
userObj = Users(url="https://api.openbrewerydb.org/v1/breweries")
print(userObj.fetchData())
print(userObj.getNames())