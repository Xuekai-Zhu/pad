def solution():
    total_days = 6 * 4 # Jodi walks 6 days each week for 4 weeks
    total_distance = 0

    for i in range(1, 5):
        distance_per_day = i
        total_distance += distance_per_day * 6

    result = total_distance
    return result

print(solution())