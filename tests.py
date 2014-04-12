# -*- coding: utf-8 -*-

import unittest

from blackskirt import (WEEKDAY_MON, WEEKDAY_TUE, WEEKDAY_WED, WEEKDAY_THU,
                        WEEKDAY_FRI, WEEKDAY_SAT, WEEKDAY_SUN)
from blackskirt.blackskirt import (next_weekday, prev_weekday, nearest_weekday,
                                   nth_weekday, last_weekday, next_date,
                                   prev_date, nearest_date, mondayise,)


class TestBlackskirt(unittest.TestCase):
    def test_next_weekday(self):
        self.assertEqual(next_weekday("2014-01-01", weekday=WEEKDAY_WED),
                         "2014-01-08")
        self.assertEqual(next_weekday("2014-01-01", weekday=WEEKDAY_THU),
                         "2014-01-02")
        self.assertEqual(next_weekday("2014-01-01", weekday=WEEKDAY_TUE),
                         "2014-01-07")

    def test_prev_weekday(self):
        self.assertEqual(prev_weekday("2014-01-01", weekday=WEEKDAY_WED),
                         "2013-12-25")
        self.assertEqual(prev_weekday("2014-01-01", weekday=WEEKDAY_THU),
                         "2013-12-26")
        self.assertEqual(prev_weekday("2014-01-01", weekday=WEEKDAY_TUE),
                         "2013-12-31")

    def test_nearest_weekday(self):
        self.assertEqual(nearest_weekday("2014-01-01", weekday=WEEKDAY_WED),
                         "2014-01-01")
        self.assertEqual(nearest_weekday("2014-01-01", weekday=WEEKDAY_SAT),
                         "2014-01-04")
        self.assertEqual(nearest_weekday("2014-01-01", weekday=WEEKDAY_SUN),
                         "2013-12-29")
        self.assertEqual(nearest_weekday("2014-01-01", weekday=WEEKDAY_SAT),
                         "2014-01-04")
        self.assertEqual(nearest_weekday("2014-01-01", weekday=WEEKDAY_SUN),
                         "2013-12-29")

    def test_nth_weekday(self):
        # year: 2014, month: 01, weekday: wed
        self.assertEqual(nth_weekday(2014, 1, n=1, weekday=WEEKDAY_WED),
                         "2014-01-01")
        self.assertEqual(nth_weekday(2014, 1, n=2, weekday=WEEKDAY_WED),
                         "2014-01-08")
        self.assertEqual(nth_weekday(2014, 1, n=3, weekday=WEEKDAY_WED),
                         "2014-01-15")
        self.assertEqual(nth_weekday(2014, 1, n=4, weekday=WEEKDAY_WED),
                         "2014-01-22")
        self.assertEqual(nth_weekday(2014, 1, n=5, weekday=WEEKDAY_WED),
                         "2014-01-29")

        # year: 2014, month: 01, weekday: sun
        self.assertEqual(nth_weekday(2014, 1, n=1, weekday=WEEKDAY_SUN),
                         "2014-01-05")
        self.assertEqual(nth_weekday(2014, 1, n=2, weekday=WEEKDAY_SUN),
                         "2014-01-12")
        self.assertEqual(nth_weekday(2014, 1, n=3, weekday=WEEKDAY_SUN),
                         "2014-01-19")
        self.assertEqual(nth_weekday(2014, 1, n=4, weekday=WEEKDAY_SUN),
                         "2014-01-26")

    def test_last_weekday(self):
        self.assertEqual(last_weekday(2014, 1, weekday=WEEKDAY_FRI),
                         "2014-01-31")
        self.assertEqual(last_weekday(2014, 1, weekday=WEEKDAY_THU),
                         "2014-01-30")
        self.assertEqual(last_weekday(2014, 1, weekday=WEEKDAY_SAT),
                         "2014-01-25")

    def test_next_date(self):
        self.assertEqual(next_date(12, 31, offset="2014-01-01"),
                         "2014-12-31")
        self.assertEqual(next_date(1, 1, offset="2014-01-01"),
                         "2015-01-01")
        self.assertEqual(next_date(1, 2, offset="2014-01-01"),
                         "2014-01-02")

    def test_prev_date(self):
        self.assertEqual(prev_date(1, 1, offset="2014-01-01"),
                         "2013-01-01")
        self.assertEqual(prev_date(12, 31, offset="2014-01-01"),
                         "2013-12-31")
        self.assertEqual(prev_date(1, 2, offset="2014-01-01"),
                         "2013-01-02")

    def test_nearest_date(self):
        self.assertEqual(nearest_date(1, 1, offset="2014-01-01"),
                         "2014-01-01")
        self.assertEqual(nearest_date(12, 31, offset="2014-01-01"),
                         "2013-12-31")
        self.assertEqual(nearest_date(1, 2, offset="2014-01-01"),
                         "2014-01-02")
        self.assertEqual(nearest_date(7, 2, offset="2014-01-01"),
                         "2014-07-02")
        self.assertEqual(nearest_date(7, 3, offset="2014-01-01"),
                         "2013-07-03")

    def test_mondayise(self):
        self.assertEqual(mondayise("2014-01-04",
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise("2014-01-05",
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise("2014-01-06",
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-06")
        self.assertEqual(mondayise("2014-01-07",
                                   cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))),
                         "2014-01-07")


if __name__ == "__main__":
    unittest.main()
