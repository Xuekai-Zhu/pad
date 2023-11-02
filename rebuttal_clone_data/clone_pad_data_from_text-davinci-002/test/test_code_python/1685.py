def solution():
    fences_built = 10
    minutes_per_fence = 30
    hours_worked = 8
    fences_per_hour = 60 / minutes_per_fence
    total_fences = fences_built + (fences_per_hour * hours_worked)
    result = total_fences
    return result

print(solution())