# Built-in
from typing import List
from time import sleep

# Custom
from simple_stopwatch import simple_stopwatch


sw = simple_stopwatch()

title_list: List[str] = []
for time in [0.1, 0.3, 0.6, 0.9]:
    sw.start_timer()
    sleep(time)
    sw.stop_timer()

    title_list.append(f"Sleep for {time} seconds")

sw.print_results(timer_titles=title_list)
