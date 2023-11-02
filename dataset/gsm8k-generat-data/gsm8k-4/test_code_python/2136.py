def solution():
    """Jessica just got her driving permit. She must complete 50 hours of driving with a parent to get her driver’s license. It takes 20
    minutes to drive to school. If she drives to and from school every day, how many school days will it take Jessica to meet the 50-hour driving requirement?"""
    # Define the time it takes to drive to school and back
    round_trip_time = 20 * 2  # 40 minutes

    # Define the number of hours of driving per school day
    hours_per_day = round_trip_time / 60  # 0.67 hours

    # Calculate the number of school days required to reach 50 hours of driving
    school_days = 50 / hours_per_day

    result = round(school_days)
    return result

print(solution())