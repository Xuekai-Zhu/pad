def solution():
    """The city’s bus system carries 1,200,000 people each day. How many people does the bus system carry for 13 weeks?"""
    # Define the number of days in a week and the number of weeks
    DAYS_PER_WEEK = 7
    WEEKS = 13

    # Calculate the total number of people the bus system carries
    total_people = 1_200_000 * DAYS_PER_WEEK * WEEKS

    # Display the total number of people
    result = total_people
    return result

print(solution())