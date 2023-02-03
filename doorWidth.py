#this will give the reccomended minimum sensor height based off the installation guide as well as output what the standard mount height is for the calculation
#it then checks to see if there is enough room for each type of mount

from oneSensorDictImp import stealth_check1
from twoSensorDictImp import stealth_check2
from threeSensorDictImp import stealth_check3
from oneSensorDictMet import stealth_check4
from twoSensorDictMet import stealth_check5
from threeSensorDictMet import stealth_check6

def doorWidthImp(n, thresholdWidth):

  '''This function takes the standard mount height in imperial or metric and threshold width then uses a function with a dictionary to determine the minimum mount height.
  After it will check to see if we need to add another sensor or move to the next function in our program. Each dictionary was made with the specifications on the
  installation guide.'''

  if n == 1:
    minMountHeightImp = stealth_check1[thresholdWidth]
    print(f'The recommended sensor height for n = 1 sensor based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightImp}.')
  #check here which one is less, the smaller one is the one we want to run through this function
  elif n == 2:
    minMountHeightImp = stealth_check2[thresholdWidth]
    print(f'The recommended sensor height for n = 2 sensors based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightImp}.')
  elif n == 3:
    minMountHeightImp = stealth_check3[thresholdWidth]
    print(f'The recommended sensor height for n = 3 sensors based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightImp}.')
  return minMountHeightImp, thresholdWidth

def doorWidthMet(n, thresholdWidth):
  if n == 1:
    minMountHeightMet = stealth_check4[thresholdWidth]
    print(f'The recommended sensor height for n = 1 sensor based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightMet}.')
  #check here which one is less, the smaller one is the one we want to run through this function
  elif n == 2:
    minMountHeightMet = stealth_check5[thresholdWidth]
    print(f'The recommended sensor height for n = 2 sensors based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightMet}.')
  elif n == 3:
    minMountHeightMet = stealth_check6[thresholdWidth]
    print(f'The recommended sensor height for n = 3 sensors based off of the installation guidelines for a door width of {thresholdWidth} is {minMountHeightMet}.')
  return minMountHeightMet, thresholdWidth