#AFTER OUTPUTTING SENSOR COUNT ON LOGIC CHART
#Imperial
#MPI = Multi Point Installation

from sensorSpacingFormula import getSensorSpacing

def mpi(mountHeightFinal, units, value, isDoor, isCorr):

  '''This function takes in the final mount height and units then asks a set of questions inculding if there are multiple sensors being installed. This will give the specifications on where to mount
  and sensor spacing if n < 1. This end one side of the calculation.'''

  if units == "imperial":
    if value == 'no':
      if mountHeightFinal> 100:
        if isDoor == 'yes':
          if isCorr == 'yes':
            print('Centered')
            print('Horizontal Alignment')
          elif isCorr == 'no':
            print('Offset 10"')
            print('Horizontal Alignment')
        elif isDoor == 'no':
          print('Centered')
          print('Horizontal Alignment')
      else:
        print('Centered')
        print('Horizontal Alignment')
    elif value == 'yes':
      sensorSpacing = getSensorSpacing(mountHeightFinal)
      print(f'Sensor spacing is {sensorSpacing} inches')
    else:
      print('Please enter yes or no')
  elif units == 'metric':
    if value == 'no':
      if mountHeightFinal > 254:
        if isDoor == 'yes':
          if isCorr == 'yes':
            print('Centered')
            print('Horizontal Alignment')
          elif isCorr == 'no':
            print('Offset 10"')
            print('Horizontal Alignment')
        elif isDoor == 'no':
          print('Centered')
          print('Horizontal Alignment')
      else:
        print('Centered')
        print('Horizontal Alignment')
    elif value == 'yes':
      sensorSpacing = getSensorSpacing(mountHeightFinal)
      print(f'Sensor spacing is {sensorSpacing} centimeters')
    else:
      print('Please enter yes or no')