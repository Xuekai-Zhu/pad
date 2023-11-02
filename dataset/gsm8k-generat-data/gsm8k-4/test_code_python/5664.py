def solution():
    """Miriam takes care of the flowers in the botanical garden. She works 5 hours a day and can take care of 60 different flowers in one day. How many flowers can Miriam take care of in 6 days of work?"""
    # Define the number of hours Miriam works each day and the number of flowers she can take care of in one day
    HOURS_PER_DAY = 5
    FLOWERS_PER_DAY = 60

    # Calculate the total number of flowers Miriam can take care of in 6 days
    flowers_total = FLOWERS_PER_DAY * 6

    # Calculate the number of flowers Miriam can take care of each hour
    flowers_per_hour = flowers_total / (6 * HOURS_PER_DAY)

    result = flowers_total
    return result

print(solution())