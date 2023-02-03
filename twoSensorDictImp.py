#for two sensors imperial

class RangeDictTwoSensorImp(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
stealth_check2 = RangeDictTwoSensorImp({range(1,69): 92, range(69,75): 94, range(75,81): 96, range(81, 87): 98, range(87, 93): 100,
                           range(93, 99): 102, range(99,105): 104, range(105,111): 106, range(111,117): 108, range(117, 123): 110,
                           range(123,129): 112, range(129,135): 114, range(135, 141): 116, range(141,147): 118})