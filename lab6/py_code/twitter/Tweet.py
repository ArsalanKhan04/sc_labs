from datetime import datetime
from typing import Any


class Tweet:
    def __init__(self, id: int, author: str, text: str, timestamp: datetime):
        self._id = id
        self._author = author
        self._text = text
        self._timestamp = timestamp
        
        # Representation invariant checks
        assert len(self._author) > 0, "Author must not be empty."
        assert all(c.isalnum() or c in {'_', '-'} for c in self._author), "Invalid characters in author."
        assert len(self._text) <= 140, "Text must be 140 characters or less."

    @property
    def id(self) -> int:
        return self._id

    @property
    def author(self) -> str:
        return self._author

    @property
    def text(self) -> str:
        return self._text

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def __str__(self) -> str:
        return f"({self.id} {self.timestamp.isoformat()} {self.author}) {self.text}"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Tweet):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

