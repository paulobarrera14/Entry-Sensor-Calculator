#for one sensor

class RangeDictOneSensorImp(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

stealth_check1 = RangeDictOneSensorImp({range(1,41): 92, range(41,46): 93, range(46,51): 96, range(51, 56): 99, range(56, 61): 102,
                           range(61, 66): 105, range(66,71): 108, range(71,76): 111, range(76,81): 114, range(81, 86): 117,
                           range(86,91): 118})