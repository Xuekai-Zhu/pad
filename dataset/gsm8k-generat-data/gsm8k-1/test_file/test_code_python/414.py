def solution():
    """Zack's locker is half as big as Timothy's locker. Peter's locker is 1/4 as big as Zack's locker. If Peter's locker is 5 cubic inches, how big is Timothy's locker in cubic inches?"""
    peter_locker = 5
    zack_locker = peter_locker * 4
    timothy_locker = zack_locker * 2
    result = timothy_locker
    return result

print(solution())