# -*- coding: utf-8 -*-

import unittest

from blackskirt import (WEEKDAY_MON, WEEKDAY_TUE, WEEKDAY_WED, WEEKDAY_THU,
                        WEEKDAY_FRI, WEEKDAY_SAT, WEEKDAY_SUN)
from blackskirt.ops import (next_weekday, prev_weekday, nearest_weekday,
                            nth_weekday, last_weekday, next_date,
                            prev_date, nearest_date, mondayise,)


class TestBlackskirt(unittest.TestCase):
    def test_next_weekday(self):
        self.assertEqual(next_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_WED),
                         "2014-01-08")
        self.assertEqual(next_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_THU),
                         "2014-01-02")
        self.assertEqual(next_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_TUE),
                         "2014-01-07")

    def test_prev_weekday(self):
        self.assertEqual(prev_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_WED),
                         "2013-12-25")
        self.assertEqual(prev_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_THU),
                         "2013-12-26")
        self.assertEqual(prev_weekday(year=2014, month=1, day=1,
                                      weekday=WEEKDAY_TUE),
                         "2013-12-31")

    def test_nearest_weekday(self):
        self.assertEqual(nearest_weekday(year=2014, month=1, day=1,
                                         weekday=WEEKDAY_WED),
                         "2014-01-01")
        self.assertEqual(nearest_weekday(year=2014, month=1, day=1,
                                         weekday=WEEKDAY_SAT),
                         "2014-01-04")
        self.assertEqual(nearest_weekday(year=2014, month=1, day=1,
                                         weekday=WEEKDAY_SUN),
                         "2013-12-29")
        self.assertEqual(nearest_weekday(year=2014, month=1, day=1,
                                         weekday=WEEKDAY_SAT),
                         "2014-01-04")
        self.assertEqual(nearest_weekday(year=2014, month=1, day=1,
                                         weekday=WEEKDAY_SUN),
                         "2013-12-29")

    def test_nth_weekday(self):
        # year: 2014, month: 01, weekday: wed
        self.assertEqual(nth_weekday(year=2014, month=1, n=1,
                                     weekday=WEEKDAY_WED),
                         "2014-01-01")
        self.assertEqual(nth_weekday(year=2014, month=1, n=2,
                                     weekday=WEEKDAY_WED),
                         "2014-01-08")
        self.assertEqual(nth_weekday(year=2014, month=1, n=3,
                                     weekday=WEEKDAY_WED),
                         "2014-01-15")
        self.assertEqual(nth_weekday(year=2014, month=1, n=4,
                                     weekday=WEEKDAY_WED),
                         "2014-01-22")
        self.assertEqual(nth_weekday(year=2014, month=1, n=5,
                                     weekday=WEEKDAY_WED),
                         "2014-01-29")

        # year: 2014, month: 01, weekday: sun
        self.assertEqual(nth_weekday(year=2014, month=1, n=1,
                                     weekday=WEEKDAY_SUN),
                         "2014-01-05")
        self.assertEqual(nth_weekday(year=2014, month=1, n=2,
                                     weekday=WEEKDAY_SUN),
                         "2014-01-12")
        self.assertEqual(nth_weekday(year=2014, month=1, n=3,
                                     weekday=WEEKDAY_SUN),
                         "2014-01-19")
        self.assertEqual(nth_weekday(year=2014, month=1, n=4,
                                     weekday=WEEKDAY_SUN),
                         "2014-01-26")

    def test_last_weekday(self):
        self.assertEqual(last_weekday(year=2014, month=1, weekday=WEEKDAY_FRI),
                         "2014-01-31")
        self.assertEqual(last_weekday(year=2014, month=1, weekday=WEEKDAY_THU),
                         "2014-01-30")
        self.assertEqual(last_weekday(year=2014, month=1, weekday=WEEKDAY_SAT),
                         "2014-01-25")

    def test_next_date(self):
        self.assertEqual(next_date(month=12, day=31, offset=(2014, 1, 1)),
                         "2014-12-31")
        self.assertEqual(next_date(month=1, day=1, offset=(2014, 1, 1)),
                         "2015-01-01")
        self.assertEqual(next_date(month=1, day=2, offset=(2014, 1, 1)),
                         "2014-01-02")

    def test_prev_date(self):
        self.assertEqual(prev_date(month=1, day=1, offset=(2014, 1, 1)),
                         "2013-01-01")
        self.assertEqual(prev_date(month=12, day=31, offset=(2014, 1, 1)),
                         "2013-12-31")
        self.assertEqual(prev_date(month=1, day=2, offset=(2014, 1, 1)),
                         "2013-01-02")

    def test_nearest_date(self):
        self.assertEqual(nearest_date(month=1, day=1, offset=(2014, 1, 1)),
                         "2014-01-01")
        self.assertEqual(nearest_date(month=12, day=31, offset=(2014, 1, 1)),
                         "2013-12-31")
        self.assertEqual(nearest_date(month=1, day=2, offset=(2014, 1, 1)),
                         "2014-01-02")
        self.assertEqual(nearest_date(month=7, day=2, offset=(2014, 1, 1)),
                         "2014-07-02")
        self.assertEqual(nearest_date(month=7, day=3, offset=(2014, 1, 1)),
                         "2013-07-03")

    def test_mondayise(self):
        self.assertEqual(mondayise(year=2014, month=1, day=4,
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise(year=2014, month=1, day=5,
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise(year=2014, month=1, day=6,
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise(year=2014, month=1, day=7,
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-07")


if __name__ == "__main__":
    unittest.main()
