def solution():
    # Calculate the total time spent rounding the island over the weekend
    time_per_round = 30  # minutes
    rounds_on_saturday = 10
    rounds_on_sunday = 15
    total_rounds = 1 + rounds_on_saturday + rounds_on_sunday  # 1 round on Saturday + 10 rounds on Saturday + 15 rounds on Sunday
    total_time = total_rounds * time_per_round  # Total time spent rounding the island
    result = total_time
    return result

print(solution())