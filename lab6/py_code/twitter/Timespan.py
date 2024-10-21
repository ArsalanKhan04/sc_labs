from datetime import datetime
from typing import Any


class Timespan:
    def __init__(self, start: datetime, end: datetime):
        if start > end:
            raise ValueError("Requires start <= end")
        self._start = start
        self._end = end

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def end(self) -> datetime:
        return self._end

    def __str__(self) -> str:
        return f"[{self.start.isoformat()}...{self.end.isoformat()}]"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Timespan):
            return False
        return self.start == other.start and self.end == other.end

    def __hash__(self) -> int:
        return hash((self.start, self.end))

