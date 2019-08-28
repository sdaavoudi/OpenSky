import requests 
import math 

def main():
    URL = "https://opensky-network.org/api/states/all"

    # sending get request and saving the response as response object 
    response = requests.get(url = URL) 
    print(response)

    # getting data
    data = response.json()
    dataSate = data['states']
    
    # get user's input 
    longitude_float, latitude_float = getUserInputs()

    # find and print output
    findClosestAirplane(dataSate,longitude_float,latitude_float)

def getUserInputs():
    longitude = input("enter a longitude: ")
    latitude = input("enter a latitude: ")
    return longitude, latitude

def findClosestAirplane(dataSate,inputLong,inputLat):
    
    # dictionary from distance to output information
    distanceOutputDictionary = {}
    for eachState in dataSate:
        if eachState[5]==None and eachState[6]==None:
            longitude_float = 0
            latitude_float = 0
        else:
            longitude_float = eachState[5]
            latitude_float = eachState[6]
        distance  = math.sqrt((longitude_float-inputLong)**2+(latitude_float-inputLat)**2)
        distanceOutputDictionary[distance]=[eachState[0], eachState[5], eachState[6], eachState[1],eachState[13],eachState[16]]

    # finding min distance
    minimum = 1.18973149536e+4932
    for key in distanceOutputDictionary:
        if minimum > key:
            minimum = key
    print(distanceOutputDictionary[minimum])

if __name__ == "__main__":
    main()
