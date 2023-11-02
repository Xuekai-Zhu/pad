def solution():
    paul_daily = 20
    bruce_daily = paul_daily / 2
    paul_sunday = paul_daily * 2
    bruce_sunday = paul_sunday * 2 / 2
    paul_weekly = paul_daily * 6 + paul_sunday
    bruce_weekly = bruce_daily * 6 + bruce_sunday
    difference = paul_weekly - bruce_weekly
    result = difference
    return result

print(solution())