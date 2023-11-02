def solution():
    peter_locker_volume = 5  # Peter's locker is 5 cubic inches
    zack_locker_volume = peter_locker_volume / 4  # Zack's locker is 1/4 as big as Peter's locker
    timothy_locker_volume = zack_locker_volume / 2  # Timothy's locker is half as big as Zack's locker

    result = timothy_locker_volume
    return result

print(solution())