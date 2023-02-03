SENSOR_SPACING_FORMULA = {'slope': 1.5, 'yIntercept': -113};


def getSensorSpacing(mountHeight):
    return ((SENSOR_SPACING_FORMULA['slope'] * mountHeight + SENSOR_SPACING_FORMULA['yIntercept']))