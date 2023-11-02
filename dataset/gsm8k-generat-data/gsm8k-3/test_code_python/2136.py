def solution():
    """Jessica just got her driving permit. She must complete 50 hours of driving with a parent to get her driver’s license. It takes 20 minutes to drive to school. If she drives to and from school every day, how many school days will it take Jessica to meet the 50-hour driving requirement?"""
    # Convert 20 minutes to hours
    travel_time = 20 / 60

    # Calculate the hours of driving per school day
    daily_driving = travel_time * 2

    # Calculate the number of school days needed to reach 50 hours of driving
    days_needed = 50 / daily_driving

    # Round up to the nearest whole number of school days
    total_days = math.ceil(days_needed)

    # Display the total number of school days needed
    result = total_days
    return result

print(solution())