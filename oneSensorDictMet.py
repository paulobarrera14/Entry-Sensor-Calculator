#for one sensors metric

class RangeDictOneSensorMet(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
stealth_check4 = RangeDictOneSensorMet({range(1,102): 232, range(102,115): 236, range(115,128): 244, range(128, 141): 251, range(141, 154): 259,
                           range(154, 167): 266, range(167,179): 274, range(179,192): 282, range(192,204): 290, range(204, 217): 297,
                           range(217,230): 300})