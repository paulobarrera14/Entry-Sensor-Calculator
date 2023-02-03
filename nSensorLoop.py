from doorWidth import doorWidthImp
from doorWidth import doorWidthMet
from checkMinMountHeight import checkMinMountHeightImp
from checkMinMountHeight import checkMinMountHeightMet

def nSensorLoop(units, mountHeightFinal, n, doorHeight, ceilingHeight, thresholdWidth, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount):

    '''nSensorLoop is the first check that determines if we need to add another sensor or can use the recommended height in our next check. If the mount height
    is greater than 118 and the threshold width is less than 210 it will add another sensor then redo the calculation until we reach max number of sensors or it
    is determined that we cannot mount.'''

    if units == 'imperial':
        while n <= 3:
            if mountHeightFinal <= 118:
                checkMinMountHeightImp(mountHeightFinal, n, doorHeight, units, ceilingHeight, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
                break
            else:
                if thresholdWidth > 210:
                    print('Cannot Mount, threshold width cannot be greater than 210 inches')
                else:
                    n = n + 1
                    continue
        if n > 3:
            print('Cannot Mount, sensor count cannot be greater than 3')

    elif units == 'metric':
        while n <= 3:
            #
            if mountHeightFinal <= 300:
                checkMinMountHeightMet(mountHeightFinal, n, doorHeight, units, ceilingHeight, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
                break
            else:
                if thresholdWidth > 533:
                    print('Cannot Mount, threshold width cannot be greater than 533 centimeters')
                else:
                    n = n + 1
                    continue
        if n > 3:
            print('Cannot Mount, sensor count cannot be greater than 3')

