# time-stamp
Python module to write and check a time stamp

This is just an example of how to use tinydb. However, for such an easy task I would rather use pickle without a databse.

Import the module like this:

import t_stamp

To write a the current date and time as a time stamp:

t_stamp.write_ts()

To check that a certain time period (eg. 3 hours) has elapsed in seconds:

elapsed = 3 * 60 * 60

if t_stamp.too_recent(elapsed):
  do something ...
