#added a step to make this function not needed but keeping it incase we need it for later

def mountPossibilityCheckImp(standMountHeightImp):
  #standard wall mount needs atleast 6.75 inches above door
  #for ceiling mount the sensor cannot hang below the height of the door
  #minimum sensor height 92 inches, maximum is 118 inches
  wallSpace = ceilingHeight - doorHeight
  if wallSpace >= 6.75:
    print("Standard Wall Mount is Possible")
    print(f"Ceiling Mount height is {standMountHeightImp} inches")
  elif wallSpace < 6.75 and wallSpace + doorHeight > 92 and wallSpace + doorHeight < 118:
    print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
    print(f"Ceiling Mount height is {standMountHeightImp} inches")
    return True
  else:
    print("Standard Wall Mount and Ceiling Mount are not Possible")
    return False

def mountPossibilityCheckMet(standMountHeightMet):
  wallSpace = ceilingHeight - doorHeight
  if wallSpace >= 17.1:
    print("Standard Wall Mount is Possible")
    print(f"Ceiling Mount height is {standMountHeightImp} inches")
  elif wallSpace < 6.75 and wallSpace + doorHeight > 92 and wallSpace + doorHeight < 118:
    print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
    print(f"Ceiling Mount height is {standMountHeightMet} inches")
    return True
  else:
    print("Standard Wall Mount and Ceiling Mount are not Possible")
    return False