def solution():
    # Number of coins added in the first hour
    hour1 = 20

    # Number of coins added in the next two hours
    hour2 = hour3 = 30

    # Number of coins added in the fourth hour
    hour4 = 40

    # Total number of coins added in the first four hours
    total_added = hour1 + hour2 + hour3 + hour4

    # Coins taken out in the fifth hour
    hour5 = 20

    # Total number of coins left after the fifth hour
    total_left = total_added - hour5
    result = total_left
    return result

print(solution())