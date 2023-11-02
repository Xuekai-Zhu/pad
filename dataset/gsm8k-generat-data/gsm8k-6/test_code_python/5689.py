def solution():
    bunnies = 20  # number of bunnies
    frequency = 3  # number of times a bunny comes out of its burrow per minute
    minutes_in_10_hours = 10 * 60  # number of minutes in 10 hours
    total_times = bunnies * frequency * minutes_in_10_hours  # calculate the total number of times the bunnies come out of their burrows
    result = total_times
    return result

print(solution())