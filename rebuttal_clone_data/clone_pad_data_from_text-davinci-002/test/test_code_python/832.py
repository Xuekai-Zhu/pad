def solution():
    troy_distance = 75
    emily_distance = 98
    days = 5
    troy_total_distance = troy_distance * 2 * days
    emily_total_distance = emily_distance * 2 * days
    difference = emily_total_distance - troy_total_distance
    result = difference
    return result

print(solution())