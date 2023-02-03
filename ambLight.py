from doorWidth import doorWidthImp
from doorWidth import doorWidthMet

def ambLight(units, thresholdWidth, isAmbLight):
  
  '''This function comes after we get outputs for the mount height and mount type. It asks the user if there is any ambient light
  then begins to determine how many sensors need to be installed. Based off of the units it goes into the doorWidth() function that considers the value for n
  or how many sensors are recommended that will untimatly pull a value from its respective dictionary based off of the installation guide.'''
  
  #defining if there is ambient light or not, this the first instance of determining sensor number
  if isAmbLight.lower() == 'yes':
    print('Start sensor count at n = 2')
    n = 2
    if units == 'imperial':
      minMountHeightImp, thresholdWidth = doorWidthImp(n, thresholdWidth)
      return minMountHeightImp, n, thresholdWidth
    elif units == 'metric':
      minMountHeightMet, thresholdWidth = doorWidthMet(n, thresholdWidth)
      return minMountHeightMet, n, thresholdWidth
  elif isAmbLight.lower() == 'no':
    print('Start Sensor count at n = 1')
    n = 1
    if units == 'imperial':
      minMountHeightImp, thresholdWidth = doorWidthImp(n, thresholdWidth)
      return minMountHeightImp, n, thresholdWidth
    elif units == 'metric':
      minMountHeightMet, thresholdWidth = doorWidthMet(n, thresholdWidth)
      return minMountHeightMet, n, thresholdWidth
  else:
    print('Please enter yes or no')