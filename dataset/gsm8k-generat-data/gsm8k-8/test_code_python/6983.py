def solution():
    # Calculate the number of minutes the Ferris wheel is open
    total_minutes = (7 - 1) * 60

    # Calculate the number of 20-minute cycles in that time
    cycles = total_minutes // 20

    # Calculate the total number of people who can ride in those cycles
    total_riders = cycles * 70

    result = total_riders
    return result

print(solution())