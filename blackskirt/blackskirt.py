# -*- coding: utf-8 -*-

from blackskirt import WEEKDAY_MON, WEEKDAY_SAT, WEEKDAY_SUN
from blackskirt.lib import ops


def mondayise(d, cases=((WEEKDAY_SAT, WEEKDAY_MON),
                        (WEEKDAY_SUN, WEEKDAY_MON))):
    wd = ops.find_weekday(d)
    return ops.next(d, weekday=dict(cases)[wd]) if wd in dict(cases) else d


next_weekday = ops.next
prev_weekday = ops.prev
nearest_weekday = ops.nearest
nth_weekday = ops.nth
last_weekday = ops.last


if __name__ == "__main__":
    assert mondayise("2014-01-04",
                     cases=((WEEKDAY_SAT, WEEKDAY_MON),
                            (WEEKDAY_SUN, WEEKDAY_MON))) == "2014-01-06"
    assert mondayise("2014-01-05",
                     cases=((WEEKDAY_SAT, WEEKDAY_MON),
                            (WEEKDAY_SUN, WEEKDAY_MON))) == "2014-01-06"
    assert mondayise("2014-01-06",
                     cases=((WEEKDAY_SAT, WEEKDAY_MON),
                            (WEEKDAY_SUN, WEEKDAY_MON))) == "2014-01-06"
    assert mondayise("2014-01-07",
                     cases=((WEEKDAY_SAT, WEEKDAY_MON),
                            (WEEKDAY_SUN, WEEKDAY_MON))) == "2014-01-07"
