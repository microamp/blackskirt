# -*- coding: utf-8 -*-

from sys import version_info
from datetime import datetime, timedelta
from calendar import monthrange
from operator import sub, add, neg, gt, ge, lt, mul
from functools import partial

from blackskirt import DATE_FORMAT, WEEKDAYS, WEEKDAY_MON

if version_info[0] == 2:
    from string import zfill
else:
    zfill = str.zfill
    from functools import reduce


def _diff(x, y):
    return abs(sub(x, y))


def _diff_next(wd1, wd2, inclusive=False):
    diff = _diff(wd1, wd2)
    return (diff
            if partial(ge if inclusive else gt, sub(wd2, wd1), 0)() else
            sub(WEEKDAYS, diff))


def _diff_prev(wd1, wd2, inclusive=False):
    diff = _diff(wd1, wd2)
    return neg(diff
               if partial(ge if inclusive else gt, sub(wd1, wd2), 0)() else
               sub(WEEKDAYS, diff))


def _strfy(year, month, day):
    return "{year}-{month}-{day}".format(year=year,
                                         month=zfill(str(month), 2),
                                         day=zfill(str(day), 2))


def find_weekday(d, format=DATE_FORMAT):
    return datetime.strptime(d, format).isoweekday()


def type_convert(f):
    def wrap(offset, **kwargs):
        rv = f(datetime.strptime(offset, DATE_FORMAT), **kwargs)
        return rv.strftime(DATE_FORMAT)

    return wrap


@type_convert
def next(offset, weekday=WEEKDAY_MON):
    return add(offset, timedelta(days=_diff_next(offset.isoweekday(),
                                                 weekday)))


@type_convert
def prev(offset, weekday=WEEKDAY_MON):
    return add(offset, timedelta(days=_diff_prev(offset.isoweekday(),
                                                 weekday)))


@type_convert
def nearest(offset, weekday=WEEKDAY_MON):
    def _days(wd1, wd2):
        diff_next = _diff_next(wd1, wd2, inclusive=True)
        diff_prev = _diff_prev(wd1, wd2, inclusive=True)
        return diff_next if lt(abs(diff_next), abs(diff_prev)) else diff_prev

    return add(offset, timedelta(days=_days(offset.isoweekday(),
                                            weekday)))


def nth(year, month, n=1, weekday=WEEKDAY_MON):
    offset = datetime.strptime(_strfy(year, month, 1),
                               DATE_FORMAT)
    return reduce(
        add,
        (offset,
         timedelta(days=_diff_next(offset.isoweekday(),
                                   weekday,
                                   inclusive=True)),
         timedelta(days=mul(WEEKDAYS, sub(n, 1))),)
    ).strftime(DATE_FORMAT)


def last(year, month, weekday=WEEKDAY_MON):
    offset = datetime.strptime(_strfy(year, month, monthrange(year, month)[1]),
                               DATE_FORMAT)
    return add(
        offset,
        timedelta(days=_diff_prev(offset.isoweekday(),
                                  weekday,
                                  inclusive=True))
    ).strftime(DATE_FORMAT)


def next_date():
    pass


def prev_date():
    pass


def nearest_date():
    pass


if __name__ == "__main__":
    from blackskirt import (WEEKDAY_TUE, WEEKDAY_WED, WEEKDAY_THU, WEEKDAY_FRI,
                            WEEKDAY_SAT, WEEKDAY_SUN,)

    # test 'next' with 2014-01-01 (wed)
    assert next("2014-01-01", weekday=WEEKDAY_WED) == "2014-01-08"
    assert next("2014-01-01", weekday=WEEKDAY_THU) == "2014-01-02"
    assert next("2014-01-01", weekday=WEEKDAY_TUE) == "2014-01-07"

    # test 'prev' with 2014-01-01 (wed)
    assert prev("2014-01-01", weekday=WEEKDAY_WED) == "2013-12-25"
    assert prev("2014-01-01", weekday=WEEKDAY_THU) == "2013-12-26"
    assert prev("2014-01-01", weekday=WEEKDAY_TUE) == "2013-12-31"

    # test 'nearest' with '2014-01-01' (wed)
    assert nearest("2014-01-01", weekday=WEEKDAY_WED) == "2014-01-01"
    assert nearest("2014-01-01", weekday=WEEKDAY_SAT) == "2014-01-04"
    assert nearest("2014-01-01", weekday=WEEKDAY_SUN) == "2013-12-29"
    assert nearest("2014-01-01", weekday=WEEKDAY_SAT) == "2014-01-04"
    assert nearest("2014-01-01", weekday=WEEKDAY_SUN) == "2013-12-29"

    # test 'nth' with '2014-01' (wed)
    assert nth(2014, 1, n=1, weekday=WEEKDAY_WED) == "2014-01-01"
    assert nth(2014, 1, n=2, weekday=WEEKDAY_WED) == "2014-01-08"
    assert nth(2014, 1, n=3, weekday=WEEKDAY_WED) == "2014-01-15"
    assert nth(2014, 1, n=4, weekday=WEEKDAY_WED) == "2014-01-22"
    assert nth(2014, 1, n=5, weekday=WEEKDAY_WED) == "2014-01-29"

    # test 'nth' with '2014-01' (sun)
    assert nth(2014, 1, n=1, weekday=WEEKDAY_SUN) == "2014-01-05"
    assert nth(2014, 1, n=2, weekday=WEEKDAY_SUN) == "2014-01-12"
    assert nth(2014, 1, n=3, weekday=WEEKDAY_SUN) == "2014-01-19"
    assert nth(2014, 1, n=4, weekday=WEEKDAY_SUN) == "2014-01-26"

    # test 'last' with '2014-01'
    assert last(2014, 1, weekday=WEEKDAY_FRI) == "2014-01-31"
    assert last(2014, 1, weekday=WEEKDAY_THU) == "2014-01-30"
    assert last(2014, 1, weekday=WEEKDAY_SAT) == "2014-01-25"
