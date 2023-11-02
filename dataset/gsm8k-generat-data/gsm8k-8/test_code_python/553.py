def solution():
    # Define the number of school days in a week and the number of weeks in 3 weeks
    school_days_per_week = 5
    total_weeks = 3

    # Calculate the total number of school days in 3 weeks
    total_school_days = school_days_per_week * total_weeks

    # Calculate the total number of containers of milk Emma buys in 3 weeks
    total_containers = 2 * total_school_days
    result = total_containers
    return result

print(solution())