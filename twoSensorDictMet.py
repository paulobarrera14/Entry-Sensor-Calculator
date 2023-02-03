#for two sensors metric

class RangeDictTwoSensorMet(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
stealth_check5 = RangeDictTwoSensorMet({range(1,158): 232, range(158,174): 234, range(174,189): 238, range(189, 204): 245, range(204, 219): 249,
                           range(219, 235): 254, range(235,250): 259, range(250,265): 264, range(265,280): 269, range(280, 296): 274,
                           range(296,311): 279, range(311,326): 284, range(326, 341): 289, range(341,357): 295, range(357,372): 300})