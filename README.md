# SimpleStopwatch

This is a simple stopwatch to measure or compare the performance of different Python code.

---------

To install this package with pip, run the following command:

```py
python -m pip install -U git+https://github.com/hrolfurgylfa/SimpleStopwatch
```

This module can than be used to measure or compare performance of code like this:

```py
from simple_stopwatch import simple_stopwatch


sw = simple_stopwatch()

sw.start_timer()
sleep(0.5) # Do something that you want to measure
sw.stop_timer()

sw.start_timer()
sleep(0.6) # Do a second thing to measure
sw.stop_timer()

# timer_titles can be added optionally to swap out the default titles for your own ones.
sw.print_results(timer_titles=["Sleep for 0.5 seconds", "Sleep for 0.6 seconds"])
```
