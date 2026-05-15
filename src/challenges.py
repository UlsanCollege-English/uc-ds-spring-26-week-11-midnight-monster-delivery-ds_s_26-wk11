"""Week 11: Midnight Monster Delivery.

Implement Dijkstra's algorithm using a heap-based priority queue.

Rules:
- Use Python 3.11+.
- Use the standard library only.
- Use heapq for the priority queue.
- Edge weights must be positive.
"""

from math import inf


HAUNTED_CITY = {
    "Crypt Kitchen": {
        "Fog Alley": 2,
        "Bone Bridge": 5,
    },
    "Fog Alley": {
        "Moon Bridge": 1,
        "Goblin Market": 6,
    },
    "Bone Bridge": {
        "Goblin Market": 2,
    },
    "Moon Bridge": {
        "Werewolf Den": 5,
        "Goblin Market": 3,
    },
    "Goblin Market": {
        "Vampire Tower": 5,
    },
    "Werewolf Den": {
        "Vampire Tower": 2,
    },
    "Vampire Tower": {},
}


def validate_haunted_map(graph: dict[str, dict[str, int]]) -> None:
    """Raise ValueError if the haunted map is invalid.

    A valid haunted map:
    - is a dictionary
    - each node maps to a dictionary of neighbors
    - every neighbor is also a node in the graph
    - every edge weight is positive

    Args:
        graph: Weighted graph represented as an adjacency dictionary.

    Raises:
        ValueError: If the graph is invalid.
    """
    # TODO: Implement this function.
    raise NotImplementedError


def monster_delivery_costs(
    graph: dict[str, dict[str, int]],
    start: str,
) -> dict[str, float]:
    """Return the cheapest delivery cost from start to every location.

    Use Dijkstra's algorithm with heapq.

    Args:
        graph: Weighted graph represented as an adjacency dictionary.
        start: Starting location.

    Returns:
        Dictionary mapping each location to its cheapest known cost.
        Unreachable locations should stay as math.inf.

    Raises:
        ValueError: If the graph is invalid or start is missing.
    """
    # TODO: Implement this function.
    raise NotImplementedError


def shortest_monster_delivery(
    graph: dict[str, dict[str, int]],
    start: str,
    target: str,
) -> tuple[float, list[str]]:
    """Return the cheapest cost and path from start to target.

    Use Dijkstra's algorithm with heapq and reconstruct the path using
    a previous-node map.

    Args:
        graph: Weighted graph represented as an adjacency dictionary.
        start: Starting location.
        target: Destination location.

    Returns:
        (cost, path), where path is in start-to-target order.
        If start or target is missing, return (math.inf, []).
        If target is unreachable, return (math.inf, []).
        If start equals target, return (0, [start]).
    """
    # TODO: Implement this function.
    raise NotImplementedError


def best_next_monster_stop(
    graph: dict[str, dict[str, int]],
    start: str,
    targets: list[str],
) -> tuple[str, float]:
    """Return the reachable target with the cheapest delivery cost.

    Stretch challenge.

    Rules:
    - Ignore unreachable targets.
    - If no target is reachable, return ("", math.inf).
    - If there is a tie, return the target that appears first in targets.

    Args:
        graph: Weighted graph represented as an adjacency dictionary.
        start: Starting location.
        targets: Possible destination locations.

    Returns:
        A tuple of (target, cost).
    """
    # TODO: Optional stretch. Implement if you want an extra challenge.
    raise NotImplementedError
