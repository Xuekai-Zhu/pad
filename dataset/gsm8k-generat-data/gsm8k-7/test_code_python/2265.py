def solution():
    initial_racers = 50
    additional_racers = 30
    race_time_1 = 20
    race_time_2 = 30
    finishers = 130

    # Calculate the number of racers at the end of the first 20 minutes
    racers_at_20min = initial_racers + additional_racers

    # Calculate the number of racers at the end of the next 30 minutes (doubled from previous)
    racers_at_50min = racers_at_20min * 2

    # Calculate the number of racers who dropped out before finishing
    dropped_racers = racers_at_50min - finishers
    result = dropped_racers
    return result

print(solution())