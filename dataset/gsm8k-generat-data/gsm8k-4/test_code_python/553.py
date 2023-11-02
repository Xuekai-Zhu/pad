def solution():
    """Emma buys 2 containers of milk every school day for lunch. She does not go to school on the weekends. How many containers of milk does she buy in 3 weeks?"""
    # Define the number of school days in a week and the number of weeks
    SCHOOL_DAYS_PER_WEEK = 5
    WEEKS = 3

    # Calculate the total number of school days in 3 weeks
    total_school_days = SCHOOL_DAYS_PER_WEEK * WEEKS

    # Calculate the total number of milk containers Emma buys in 3 weeks
    total_milk_containers = 2 * total_school_days

    # Return the result
    result = total_milk_containers
    return result

print(solution())