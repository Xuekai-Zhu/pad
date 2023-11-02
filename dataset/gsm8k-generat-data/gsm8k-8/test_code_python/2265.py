def solution():
    # Calculate the number of racers after 20 minutes
    racers_after_20_min = 50 + 30

    # Calculate the number of racers before the doubling occurred
    racers_before_doubling = racers_after_20_min

    # Calculate the number of racers after the doubling occurred
    racers_after_doubling = racers_before_doubling * 2

    # Calculate the number of racers who dropped out before finishing the race
    racers_dropped_out = racers_after_doubling - 130

    result = racers_dropped_out
    return result

print(solution())