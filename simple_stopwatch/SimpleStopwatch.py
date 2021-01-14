# Built-in
from datetime import timedelta
from typing import List, Optional
from math import ceil

# Mine
from simple_stopwatch.SimpleTimer import SimpleTimer
from simple_stopwatch.State import State
import simple_stopwatch.errors as errors


class SimpleStopwatch:
    def __init__(self) -> None:
        self._state = State.STOPPED
        self._timers: List[SimpleTimer] = []

    def start_timer(self) -> None:
        try:
            # Make sure the timer is stopped
            assert self._state == State.STOPPED

            # Set the state to running
            self._state = State.RUNNING

            # Add a timer to the list, this is done like this to make sure
            # the list doesn't have to be extended while the timer is running.
            self._timers.append(None)  # type: ignore
            self._timers[-1] = SimpleTimer(start_now=True)
        except AssertionError:
            raise errors.FunctionNotAvailableInState(
                "start_timer cannot be called while the timer is running."
            ) from None

    def stop_timer(self) -> None:
        try:
            assert self._state == State.RUNNING
            self._timers[-1].stop()
            self._state = State.STOPPED
        except AssertionError:
            raise errors.FunctionNotAvailableInState(
                "stop_timer cannot be called while the timer is stopped."
            ) from None

    @property
    def duration(self) -> timedelta:
        return sum(self.durations, timedelta())

    @property
    def durations(self) -> List[timedelta]:
        try:
            assert self._state == State.STOPPED
            return [timer.duration for timer in self._timers]
        except (errors.EarlyAttributeAccess, AssertionError):
            raise errors.EarlyAttributeAccess(
                "Please call stop_timer before accessing the duration of the stopwatch."
            ) from None

    def print_results(
        self,
        header_str: str = "Stopwatch Results",
        header_size: Optional[int] = None,  # None means auto detect size
        header_spacer_character: str = "=",
        min_header_spacer_size: int = 3,
        timer_titles: Optional[List[str]] = None,
    ) -> None:
        # Setup arguments that needed lists/dicts
        if timer_titles is None:
            timer_titles = []

        # Create the output list
        result_output_list: List[str] = []
        for i, timer in enumerate(self._timers):
            try:
                title = timer_titles[i]
            except IndexError:
                title = f"Timer {i + 1}"
            result_output_list.append(f"{title}: {timer.duration}")

        # Calculate the header
        if header_size is None:
            header_size = max(len(i) for i in result_output_list)
        header_spacer_num = int(ceil((header_size - len(header_str) - 2) / 2))
        if header_spacer_num < min_header_spacer_size:
            header_spacer_num = min_header_spacer_size
        spacer_line = header_spacer_character * header_spacer_num

        # Print the results out
        print(f"\n{spacer_line} {header_str} {spacer_line}")
        for line in result_output_list:
            print(line)
        print()
