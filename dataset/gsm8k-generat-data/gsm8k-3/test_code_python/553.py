def solution():
    """Emma buys 2 containers of milk every school day for lunch. She does not go to school on the weekends. How many containers of milk does she buy in 3 weeks?"""
    # Define the number of school days in a week
    SCHOOL_DAYS_PER_WEEK = 5

    # Define the number of weeks
    NUM_WEEKS = 3

    # Calculate the total number of school days in 3 weeks
    total_school_days = SCHOOL_DAYS_PER_WEEK * NUM_WEEKS

    # Calculate the total number of containers of milk Emma buys
    total_containers = 2 * total_school_days

    # Display the total number of containers of milk
    result = total_containers
    return result

print(solution())