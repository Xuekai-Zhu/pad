def solution():
    """Timothy's locker is 24 cubic inches. Zack's locker is half as big as Timothy's locker. Peter's locker is 1/4 as big as Zack's locker. How big is Peter's locker in cubic inches?"""
    timothy_locker = 24
    zack_locker = timothy_locker / 2
    peter_locker = zack_locker / 4
    result = peter_locker
    return result

print(solution())