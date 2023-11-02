def solution():
    # Calculate the total number of fishing days
    fishing_days = 213

    # Calculate the total number of fish caught by the first fisherman
    fisherman1_catch = 3 * fishing_days

    # Calculate the total number of fish caught by the second fisherman
    fisherman2_catch = 0

    # Calculate the number of fish caught during the first 30 days
    fisherman2_catch += 1 * 30

    # Calculate the number of fish caught during the next 60 days
    fisherman2_catch += 2 * 60

    # Calculate the number of fish caught during the remainder of the season
    fisherman2_catch += 4 * (fishing_days - 30 - 60)

    # Calculate the difference between the two catches
    difference = fisherman1_catch - fisherman2_catch
    result = difference
    return result

print(solution())