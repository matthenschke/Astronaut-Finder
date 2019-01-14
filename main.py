"""
Program that lists the number of people that are in space,
as well as their names using the ISS API
Author : Matthew Henschke
"""

# libraries used
import requests


url = "http://api.open-notify.org/astros.json" # url used to make api call

def getData():
    """ main function that makes the api call"""
    response = requests.get(url)
    data = response.json()

    def displayData():
        """ nested function that prints out the data returned by the api call"""
        numOfPeople = data["number"]
        print("API Call Info:")
        print("Response code: {}".format(response.status_code))
        print("Headers: {}".format(response.headers))
        print("\n")
        print("The number of people that are currently in space is: {}".format(numOfPeople))
        if numOfPeople > 0:
            print("The people that are currently in space are:")
            people = data['people']
            for person in people:
                print("{}, craft: {}".format(person['name'], person['craft']))

    displayData()

if __name__ == "__main__":
    getData()
