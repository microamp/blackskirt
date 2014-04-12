# -*- coding: utf-8 -*-

from datetime import datetime

from blackskirt import DATE_FORMAT, WEEKDAY_MON, WEEKDAY_SAT, WEEKDAY_SUN
from blackskirt.lib import ops


def mondayise(d, cases=((WEEKDAY_SAT, WEEKDAY_MON),
                        (WEEKDAY_SUN, WEEKDAY_MON))):
    wd = datetime.strptime(d, DATE_FORMAT).weekday()
    return ops.next(d, weekday=dict(cases)[wd]) if wd in dict(cases) else d


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
