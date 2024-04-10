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
                NameList.append(userDict["name"]["common"])
            return NameList
        else:
            print("It is not connected")

        for currency in contents["currencies"]:
                print(currency["name"])
                print(currency["symbol"])
        for currency in contents["currencies"]:
            if currency == dollar:
                print("countries")
            else:
                print("none")
        for currency in contents["currencies"]:
            if currency == Euro:
                print("countries")
            else:
                print("none")



url = "https://restcountries.com/v3.1/all"
userObj = Users(url)
print(userObj.fetchData())
print(userObj.getNames())
