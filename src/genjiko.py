from typing import List, Set, Iterator


# This method is borrowed verbatim from @olooney
# https://www.oranlooney.com/post/genji-ko/
def partitions(s: Set[int]) -> Iterator[List[Set[int]]]:
    """Yield all partitions of a set as they are generated."""
    if not s:
        yield []
        return
    first = next(iter(s))
    rest = s - {first}
    for partition in partitions(rest):
        yield [{first}] + partition
        for i in range(len(partition)):
            new_partition = (
                partition[:i] + [partition[i] | {first}] + partition[i + 1 :]
            )
            yield new_partition


class IncenseGroup:
    """Represents a set of matching incense"""

    def __init__(self, indices: Set[int], height=1.0):
        self.indices: Set = indices
        self.height: float = height

    def __str__(self):
        return f"Height {self.height:.1f}, Indices {self.indices}"

    def __repr__(self):
        return self.__str__()


class GenjiMon:
    "Represents a Genji-mon containing one or more Incense Groups"

    def __init__(self, groups: List[IncenseGroup]):
        self.groups = tuple(groups)
        self.name = "unknown"  # TODO

    def __str__(self):
        return f"GenjiMon {self.name} with {len(self.groups)} groups"

    @classmethod
    def generate_all(cls, length: int = 5) -> Iterator["GenjiMon"]:
        indices = set(range(length))
        for partition in partitions(indices):
            yield cls([IncenseGroup(sub) for sub in partition])
