def solution():
    loaves_per_hour = 5
    hours_per_week = 5
    hours_per_weekend = 2
    ovens = 4
    total_loaves = (loaves_per_hour * hours_per_week * 4 * 3) + (loaves_per_hour * hours_per_weekend * 4 * 2)
    result = total_loaves
    return result

print(solution())