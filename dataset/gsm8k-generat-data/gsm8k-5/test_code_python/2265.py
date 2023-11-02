def solution():
    # Initial number of racers
    initial_racers = 50

    # Number of racers after 20 minutes
    first_joiners = 30
    total_racers_20_min = initial_racers + first_joiners

    # Number of racers after 50 minutes
    total_racers_50_min = total_racers_20_min * 2

    # Number of racers who dropped out
    racers_dropped_out = total_racers_50_min - 130
    result = racers_dropped_out
    return result

print(solution())