def solution():
    # Calculate the distance the tiger ran before he was noticed missing
    distance_run_in_3_hours = 25 * 3  # the tiger runs at a speed of 25 mph for 3 hours before zookeepers notice he's missing
    # Calculate the distance the tiger ran before he was caught
    distance_run_before_caught = distance_run_in_3_hours + 10 * 4  # at 4 hours of running, the tiger slows down to 10 mph and runs for another 2 hours before he is chased at 50 mph for half an hour
    result = distance_run_before_caught
    return result

print(solution())