def solution():
    # Define the number of cans and rounds needed
    num_cans = 28
    num_rounds = num_cans // 4
    if num_cans % 4 != 0:
        num_rounds += 1

    # Calculate the time it takes for one round trip
    round_trip_time = 2 * 10 + 30

    # Calculate the total time needed
    total_time = num_rounds * round_trip_time

    result = total_time
    return result

print(solution())