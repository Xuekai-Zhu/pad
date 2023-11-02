def solution():
    initial_weight = 3.0
    final_weight = 1.0
    kibble_per_hour = 0.25

    # Calculate the amount of kibble the cat ate while Kira was away
    kibble_eaten = initial_weight - final_weight

    # Calculate the amount of time the cat was alone, in hours
    time_alone = kibble_eaten / kibble_per_hour
    result = time_alone
    return result

print(solution())