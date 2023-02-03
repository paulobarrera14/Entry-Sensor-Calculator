#for three sensors metric

class RangeDictThreeSensorMet(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
stealth_check6 = RangeDictThreeSensorMet({range(1,214): 232, range(214,237): 234, range(237,260): 239, range(260, 283): 245, range(283, 305): 249,
                           range(305, 329): 254, range(329,351): 259, range(351,374): 264, range(374,397): 269, range(397, 420): 274,
                           range(420,443): 279, range(443,466): 284, range(466, 489): 289, range(489,511): 295, range(511,534): 300})