Blackskirt
==========
Relative weekday/date utilities useful for finding public holidays

Installation
------------
.. code-block:: bash

    pip install blackskirt

Examples
--------
.. code-block:: python

    from blackskirt import WEEKDAY_MON, WEEKDAY_TUE, WEEKDAY_SAT, WEEKDAY_SUN
    from blackskirt.blackskirt import (mondayise, next_weekday,
                                       prev_weekday, nearest_weekday,
                                       nth_weekday, last_weekday,)

- New Year's Day: 1 January (or the following Monday if it falls on a Saturday or Sunday)
.. code-block:: python

    from blackskirt import WEEKDAY_MON, WEEKDAY_TUE, WEEKDAY_SAT, WEEKDAY_SUN
    from blackskirt.blackskirt import mondayise

    # 2011-01-01 is Saturday
    assert mondayise("2011-01-01", cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_MON))) == "2011-01-03"

- Day after New Year's Day: 2 January (or the following Monday if it falls on a Saturday, or the following Tuesday if it falls on a Sunday)
.. code-block:: python

    # 2011-01-02 is Sunday
    assert mondayise("2011-01-02", cases=((WEEKDAY_SAT, WEEKDAY_MON),
                                          (WEEKDAY_SUN, WEEKDAY_TUE))) == "2011-01-03"

- Queen's Birthday: The first Monday in June
.. code-block:: python

    assert nth_weekday(2014, 6, n=1, weekday=WEEKDAY_MON) == "2014-06-02"

License
-------
All the code is licensed under the GNU Lesser General Public License (v3+).
