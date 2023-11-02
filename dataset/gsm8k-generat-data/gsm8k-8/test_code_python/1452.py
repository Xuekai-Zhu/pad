def solution():
    # Calculate Abel's travel time in hours
    abel_time = 1000 / 50

    # Calculate Alice's travel time in hours
    alice_time = (1000 - 50) / 40

    # Calculate the difference in arrival times in minutes
    time_difference = (abel_time - alice_time) * 60

    result = time_difference
    return result

print(solution())