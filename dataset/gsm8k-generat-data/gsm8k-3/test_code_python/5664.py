def solution():
    """Miriam takes care of the flowers in the botanical garden. She works 5 hours a day and can take care of 60 different flowers in one day. How many flowers can Miriam take care of in 6 days of work?"""
    # Define Miriam's work hours and flower care rate
    HOURS_PER_DAY = 5
    FLOWERS_PER_DAY = 60

    # Calculate the total number of flowers Miriam can care for in 6 days
    total_hours = 6 * HOURS_PER_DAY
    total_flowers = FLOWERS_PER_DAY * 6

    # Display the total number of flowers
    result = total_flowers
    return result

print(solution())