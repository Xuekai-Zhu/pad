def solution():
     minnie_mounts_per_day = 3 + 7
     mickey_mounts_per_day = 2 * minnie_mounts_per_day - 6
     mickey_mounts_per_week = mickey_mounts_per_day * 7
     result = mickey_mounts_per_week
     return result

print(solution())