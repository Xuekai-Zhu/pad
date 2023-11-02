def solution():
    time_per_round = 30  # It takes the Polar Bears 30 minutes to complete one round
    rounds_on_saturday = 11  # They completed one round on Saturday, and 10 more
    rounds_on_sunday = 15  # They completed 15 more rounds on Sunday

    # Calculate the total time spent circling the island on Saturday and Sunday
    total_time = (rounds_on_saturday + rounds_on_sunday) * time_per_round
    result = total_time
    return result

print(solution())