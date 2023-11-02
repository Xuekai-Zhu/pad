def solution():
    total_flight_time = 11 * 60 + 20  # convert flight time to minutes
    time_spent = 2 * 60 + 4 * 60 + 30 + 40 + 1 * 60 + 10  # convert all time spent to minutes
    time_left = total_flight_time - time_spent  # calculate time left for nap
    nap_time = time_left / 60  # convert time left to hours
    result = nap_time
    return result

print(solution())