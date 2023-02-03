#ask user if used calculator before, if no then explain properties and outputs
from unitType import unitType
from ambLight import ambLight
from nSensorLoop import nSensorLoop

def calculator_sensor_placement(units: str, doorHeight: float, ceilingHeight: float, frameHeight: float, thresholdWidth: float,isAmbLight: str, value: str, isDoor: str, isCorr: str, isCeilingMount: str, isWallGlass: str, isDoorDeep: str, isDoorFrame: str, isWallMount: str):

    '''This calculator_sensor_placement function is the start of the calculator that takes all inputs listed below.
    We then enter the ambLight() function that has units as a variable and get three more important outputs. It then checks to see if standMountHeight or
    minMountHeight is smaller to determine which one will be mountHeightFinal. The smaller one will always be the mount height unless the value is less
    than 92 inches or 232 centimeters. nSensorLoop is then ran which takes in our outputs from earlier and does the last checks to determine sensor spacing
    if n > 1 and mount type. To find more information on the individual functions please see their individual docStrings.'''

    '''
    units: "imperial" or "metric", type:string
    doorHeight: value of door height in inches or centimeters from ground, type:float
    ceilingHeight: value of ceiling height in inches or centimeters from ground, type:float
    frameHeight: value of door frame height in inches or centimeters from ground, type:float
    thresholdWidth: value of door width in inches or centimeters, type:float
    isAmbLight: is there ambient light located near the sensor "yes" or "no", type:string
    value: is it a multi point installation "yes" or "no", type:string
    isDoor: is there a door "yes" or "no", type:string
    isCorr: is there a constraning corridor "yes" or "no", type:string
    isCeilingMount: does ceiling mount work for type of install "yes" or "no", type: string
    isWallGlass: is the wall where the install would take place glass "yes" or "no", type:string
    isDoorDeep: is the door opening deeper than 6" "yes" or "no", type:string
    isDoorFrame: is there a door frame "yes" or "no", type:string
    isWallMount: does wall mount work for type of install "yes" or "no", type:string
    '''

    units, doorHeight, ceilingHeight, standMountHeight, frameHeight = unitType(units, doorHeight, ceilingHeight, frameHeight)
    minMountHeight, n, thresholdWidth = ambLight(units, thresholdWidth, isAmbLight)
    # check here which one is less, the smaller one is the one we want to run through this function
    if units == "imperial":
        if standMountHeight >= minMountHeight >= 92 and minMountHeight <= 118:
            mountHeightFinal = minMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        elif standMountHeight <= minMountHeight <= 118 and minMountHeight >= 92:
            mountHeightFinal = minMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        elif standMountHeight >= minMountHeight and minMountHeight < 92 and standMountHeight <= 118:
            mountHeightFinal = standMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        else:
            print("Cannot Mount")
    elif units == 'metric':
        if standMountHeight >= minMountHeight >= 232 and minMountHeight <= 300:
            mountHeightFinal = minMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        elif standMountHeight <= minMountHeight <= 300 and minMountHeight >= 232:
            mountHeightFinal = minMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        elif standMountHeight >= minMountHeight and minMountHeight < 232 and standMountHeight <= 300:
            mountHeightFinal = standMountHeight
            nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        else:
            print("Cannot Mount")

    #standMountHeight or minMountHeight

calculator_sensor_placement(units='imperial', doorHeight=80, ceilingHeight=105, frameHeight=84, thresholdWidth=60, isAmbLight='yes', value='yes', isDoor='yes', isCorr='yes', isCeilingMount='yes', isWallGlass='no', isDoorDeep='no', isDoorFrame='yes', isWallMount='yes')
