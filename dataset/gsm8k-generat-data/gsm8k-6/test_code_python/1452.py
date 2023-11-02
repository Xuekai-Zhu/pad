def solution():
    # Calculate the time taken by Abel to reach the destination
    time_Abel = 1000 / 50  # Abel travels at 50 miles per hour
    # Calculate the time taken by Alice to reach the destination
    time_Alice = 1000 / 40  # Alice travels at 40 miles per hour
    # Calculate the time difference in minutes
    time_difference = (time_Abel - time_Alice) * 60
    result = time_difference
    return result

print(solution())