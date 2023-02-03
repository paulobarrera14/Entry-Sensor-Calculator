from MPI import mpi
from finalSenHeight import finalSenHeight

def checkMinMountHeightImp(mountHeightFinal, n, doorHeight, units, ceilingHeight, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount):

    '''This function is the next check in the door logic and determines if we can move on to mpi() and finalSenHeight(). The checks here are if
    ceiling or wall mount are possible. If neither are then the function prints "cannot mount."'''

    if n > 2:
        #need to check what is correct here
        mountHeightFinal = 95

        wallSpace = ceilingHeight - mountHeightFinal
        print(f"The distance in inches between the ceiling and top of the door is {wallSpace}")
        if wallSpace >= 6.75:
            print("Standard Wall Mount is Possible")
            standMountHeightImp = mountHeightFinal
            print(f"Wall Mount height is {standMountHeightImp} inches")
            mpi(standMountHeightImp, units, value, isDoor, isCorr)
            finalSenHeight(standMountHeightImp, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minMountHeightImp is 95 it will always be greater than 92
        elif wallSpace < 6.75 and wallSpace + doorHeight > 92 and wallSpace + doorHeight < 118:
            print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
            print(f"Ceiling Mount height is {mountHeightFinal} inches")
        else:
            print("CANNOT MOUNT")

    else:
        # if wall mount height is greater or equal to min mount height
        if mountHeightFinal >= 92:
            mpi(mountHeightFinal, units, value, isDoor, isCorr)
            finalSenHeight(mountHeightFinal, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        else:
            minMountHeightImp = 92
            wallSpace = ceilingHeight - minMountHeightImp
            print(f"The distance in inches between the ceiling and top of the door is {wallSpace}")
            if wallSpace >= 6.75:
                print("Standard Wall Mount is Possible")
                standMountHeightImp = minMountHeightImp
                print(f"Wall Mount height is {standMountHeightImp} inches")
                mpi(standMountHeightImp, units, value, isDoor, isCorr)
                finalSenHeight(standMountHeightImp, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minDoorHeightImp is 95 it will always be greater than 92
            elif wallSpace < 6.75 and wallSpace + doorHeight > 92 and wallSpace + doorHeight < 118:
                standMountHeightImp = minMountHeightImp
                print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
                print(f"Ceiling Mount height is {standMountHeightImp} inches")
                mpi(standMountHeightImp, units, value, isDoor, isCorr)
                finalSenHeight(standMountHeightImp, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minDoorHeightImp is 95 it will always be greater than 92
            else:
                return print("CANNOT MOUNT")

def checkMinMountHeightMet(mountHeightFinal, n, doorHeight, units, ceilingHeight, frameHeight, value, isDoor, isCorr, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount):
    if n > 2:
        mountHeightFinal = 241.3

        # here we chack if we can mount with this min door height, low profile mount is closer to the ceiling by 1.25 inches so thats why we add it here
        wallSpace = ceilingHeight - mountHeightFinal
        print(f"The distance in inches between the ceiling and top of the door is {wallSpace}")
        if wallSpace >= 17.1:
            print("Standard Wall Mount is Possible")
            standMountHeightMet = mountHeightFinal
            print(f"Wall Mount height is {standMountHeightMet} inches")
            mpi(standMountHeightMet, units, value, isDoor, isCorr)
            finalSenHeight(standMountHeightMet, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minMountHeightImp is 95 it will always be greater than 92
        elif wallSpace < 17.1 and wallSpace + doorHeight > 232 and wallSpace + doorHeight < 300:
            standMountHeightMet = mountHeightFinal
            print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
            print(f"Ceiling Mount height is {standMountHeightMet} inches")
            mpi(standMountHeightMet, units, value, isDoor, isCorr)
            finalSenHeight(standMountHeightMet, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minMountHeightImp is 95 it will always be greater than 92
        else:
            print("CANNOT MOUNT")

    else:
        # if wall mount height is greater or equal to min mount height
        if mountHeightFinal >= 232:
            mpi(mountHeightFinal, units, value, isDoor, isCorr)
            finalSenHeight(mountHeightFinal, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
        else:
            minMountHeightMet = 232
            wallSpace = ceilingHeight - minMountHeightMet
            print(f"The distance in inches between the ceiling and top of the door is {wallSpace}")
            if wallSpace >= 17.1:
                print("Standard Wall Mount is Possible")
                standMountHeightMet = minMountHeightMet
                print(f"Wall Mount height is {standMountHeightMet} inches")
                mpi(standMountHeightMet, units, value, isDoor, isCorr)
                finalSenHeight(standMountHeightMet, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minDoorHeightImp is 95 it will always be greater than 92
            elif wallSpace < 17.1 and wallSpace + doorHeight > 232 and wallSpace + doorHeight < 300:
                standMountHeightMet = minMountHeightMet
                print("Standard Wall Mount is not Possible, use a Ceiling Mount Instead")
                print(f"Ceiling Mount height is {standMountHeightMet} inches")
                mpi(standMountHeightMet, units, value, isDoor, isCorr)
                finalSenHeight(standMountHeightMet, doorHeight, units, frameHeight, isCeilingMount, isWallGlass, isDoorDeep, isDoorFrame, isWallMount)
            # go into next functions because if minDoorHeightImp is 241 it will always be greater than 232
            else:
                return print("CANNOT MOUNT")