#!/usr/bin/python3
"""A module for working with lockboxes"""
from collections import deque


def canUnlockAll(boxes):
    """Function for lockboxes"""
    n = len(boxes)
    visit = set()
    quene = deque([0])
    visit.add(0)

    while quene:
        box = quene.popleft()
        for key in boxes[box]:
            if key < n and key not in visit:
                quene.append(key)
                visit.add(key)

    return len(visit) == n
