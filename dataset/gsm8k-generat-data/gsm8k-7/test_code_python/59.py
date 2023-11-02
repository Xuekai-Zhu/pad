def solution():
    hour1 = 15
    hour2 = 35
    hour3 = 35
    hour4 = 50

    # Calculate the total number of coins collected after 4 hours
    total_collected = hour1 + hour2 + hour3 + hour4

    # Subtract the 15 coins Joanne gave to her coworker
    total_collected -= 15

    result = total_collected
    return result

print(solution())