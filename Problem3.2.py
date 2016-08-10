import math
import sys

G = 6.67e-11

def volume(radius):
   v = (4/3) * math.pi * math.pow(radius,3)
   return v
   
def mass(volume, density):
    return volume * density

def weight(distance, planetMass, objectMass):
    force = G * ((planetMass * objectMass)/(math.pow(distance,2)))
    return force

counter = 0
objectMass = 0
numberOfPlanets = 0

for line in sys.stdin:
    counter +=1
    if (counter == 1):
        objectMass = int(line)
    elif (counter == 2):
        numberOfPlanets = int(line)
    else:
        planetInfo = line.split(',')
            
        planetName = planetInfo[0]
        planetRadius = int(planetInfo[1])
        planetDensity = int(planetInfo[2])
        planetVolume = volume(planetRadius)
        planetMass = mass(planetVolume, planetDensity)
        weightOnPlanet = weight(planetRadius, planetMass, objectMass)
        
        print(planetName, ':', weightOnPlanet)
