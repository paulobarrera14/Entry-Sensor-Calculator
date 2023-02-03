#imperial
#standard wall mount needs atleast 6.75 inches above door
#for ceiling mount the sensor cannot hang below the height of the door
#minimum sensor height 92 inches, maximum is 118 inches
#MAY NEED TO ADD HEIGHT TO TOP OF DOOR FRAME

def doorInputsImp(doorHeight, ceilingHeight, frameHeight):

  '''This function stems from the units() function when imperial or metric is inputted and goes through the first relevant inputs and outputs of the calculator.
  When called it will prompt the user to enter a door height and ceiling height, from there it determines wall space and initial mounting
  possibilities such as standard mount height and ceiling mount height.'''

  if ceilingHeight - doorHeight <= 0:
    print('Review Door Inputs,  Door Height should not be greater than Ceiling Height')
  else:
    wallSpace = ceilingHeight - doorHeight
    print(f"The distance in inches between the ceiling and top of the door is {wallSpace}")
    if wallSpace >= 6.75:
      print("Standard Wall Mount is Possible")
      standMountHeightImp = ceilingHeight - 5
    elif wallSpace < 6.75 and wallSpace + doorHeight > 92 and wallSpace + doorHeight < 118:
      print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
    else:
      print("Standard Wall Mount and Ceiling Mount are not Possible")
  return doorHeight, ceilingHeight, standMountHeightImp, frameHeight

#metric
#standard wall mount needs atleast 17.1 centimeters above door
#for ceiling mount the sensor cannot hang below the height of the door
#minimum sensor height 232 centimeters, maximum is 300 centimeters
def doorInputsMet(doorHeight, ceilingHeight, frameHeight):
  '''This function stems from the units() function when metric is inputted and goes through the first relevant inputs and outputs of the calculator.
  When called it will prompt the user to enter a door height and ceiling height, from there it determines wall space and mounting
  possibilities such as standard mount height, low profile mount height and ceiling mount'''

  if ceilingHeight - doorHeight <= 0:
    print('Review Door Inputs,  Door Height should not be greater than Ceiling Height')
  else:
    wallSpace = ceilingHeight - doorHeight
    print(f"The distance in centimeters between the ceiling and top of the door is {wallSpace}")
    if wallSpace >= 17.1:
      print("Standard Wall Mount is Possible")
      standMountHeightMet = ceilingHeight - 12.7
    elif wallSpace < 17.1 and wallSpace + doorHeight > 232 and wallSpace + doorHeight < 300:
      print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
    else:
      print("Standard Wall Mount and Ceiling Mount are not Possible")
  return doorHeight, ceilingHeight, standMountHeightMet, frameHeight