#helper function
#function that determines if in metric or imperial

from doorInputs import doorInputsImp
from doorInputs import doorInputsMet

def unitType(units, doorHeight, ceilingHeight, frameHeight):

  '''This is the first function that is called in the entry calculator, here the user defines the unit type so that the program
  can go through the correct functions to output the correct units. It then calls the respective doorInputs() function for either imperial
  or metric. If imperial or metric are spelled wrong the function will break resulting in an error and print the error message. May add a continuation
  or an exeption clause if unit type is inputted incorrectly.'''

  if units.lower() == "imperial":
    doorHeight, ceilingHeight, standMountHeightImp, frameHeight = doorInputsImp(doorHeight, ceilingHeight, frameHeight)
    return units, doorHeight, ceilingHeight, standMountHeightImp, frameHeight
  elif units.lower() == "metric":
    doorHeight, ceilingHeight, standMountHeightMet, frameHeight = doorInputsMet(doorHeight, ceilingHeight, frameHeight)
    return units, doorHeight, ceilingHeight, standMountHeightMet, frameHeight

  else:
    print("Error: Please make sure your inputting valid units or if you misspelled the word")