#AFTER OUTPUTTING SENSOR HEIGHT ON LOGIC CHART
#Imperial

def finalSenHeight(mountHeightFinal, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount):

  '''This function takes in the final mount height, top of door fram height and units then asks a set of questions to determine the best
  mount type. Types can be ceiling mount, wall mount and top of door frame mount. This ends this side of the calulation and at this point the
  calculation should be finished'''

#'Is the door opening deeper than 6": ' for isDoorDeep

  if units == "imperial":
    if mountHeightFinal > 10 + int(doorHeight):
      if isCeilingMount == 'yes':
        print('Mount type is Ceiling Mount')
      elif isCeilingMount == 'no':
        if isWallGlass == "yes" and isDoorDeep == 'yes':
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} inches')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'no' and isDoorDeep == "yes":
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} inches')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'yes' and isDoorDeep == 'no':
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} inches')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'no' and isDoorDeep == 'no':
          print('Cannot Mount')
    else:
      if isWallMount == 'yes':
        print('Mount type is Wall Mount')
      elif isWallMount == 'no':
        #need to discuss what goes here
        print('Cannot Mount')
  elif units == "metric":
    if mountHeightFinal > 25.4 + int(doorHeight):
      if isCeilingMount == 'yes':
        print('Mount type is Ceiling Mount')
      elif isCeilingMount == 'no':
        if isWallGlass == "yes" and isDoorDeep == 'yes':
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} centimeters')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'no' and isDoorDeep == "yes":
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} centimeters')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'yes' and isDoorDeep == 'no':
          if isDoorFrame == 'yes':
            print(f'Mount type is Top of Door Frame Mount at {frameHeight} centimeters')
          if isDoorFrame == 'no':
            print('Cannot Mount')
        elif isWallGlass == 'no' and isDoorDeep == 'no':
          print('Cannot Mount')
    else:
      if isWallMount == 'yes':
        print('Mount type is Wall Mount')
      elif isWallMount == 'no':
        print("Cannot Mount")