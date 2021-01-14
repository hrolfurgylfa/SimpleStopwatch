from time import sleep
from typing import Optional
from datetime import datetime, timedelta
from Classes.errors import NoFunctionReuse, EarlyAttributeAccess


class SimpleTimer:
    def __init__(self, start_now: Optional[bool] = False) -> None:
        self._start_time: Optional[datetime] = None
        self._end_time: Optional[datetime] = None

        if start_now:
            self.start()

    def start(self):
        try:
            assert self._start_time is None
            self._start_time = datetime.now()
        except AssertionError:
            raise NoFunctionReuse(
                "start cannot be called multiple times on a single timer."
            ) from None

    def stop(self):
        try:
            assert self._end_time is None
            self._end_time = datetime.now()
        except AssertionError:
            raise NoFunctionReuse(
                "stop cannot be called multiple times on a single timer."
            ) from None

    @property
    def duration(self) -> timedelta:
        if self._end_time and self._start_time:
            return self._end_time - self._start_time
        else:
            raise EarlyAttributeAccess(
                "duration cannot be called before calling stop on a timer."
            )
