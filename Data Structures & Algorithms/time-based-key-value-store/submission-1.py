from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)   
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store[key]
        idx = bisect_right(entries, timestamp, key=lambda e: e[0]) - 1
        return entries[idx][1] if idx >= 0 else ""