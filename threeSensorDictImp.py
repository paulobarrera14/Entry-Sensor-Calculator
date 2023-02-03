#for three sensors imperial

class RangeDictThreeSensorImp(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

stealth_check3 = RangeDictThreeSensorImp({range(1,94): 92, range(94,103): 94, range(103,112): 96, range(112, 121): 98, range(121, 130): 100,
                           range(130, 139): 102, range(139,148): 104, range(148,157): 106, range(157,166): 108, range(166, 175): 110,
                           range(175,184): 112, range(184,193): 114, range(193, 202): 116, range(202,211): 118})