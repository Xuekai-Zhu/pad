def solution():
    """Jessica just got her driving permit. She must complete 50 hours of driving with a parent to get her driver’s license. It takes 20 minutes to drive to school. If she drives to and from school every day, how many school days will it take Jessica to meet the 50-hour driving requirement?"""
    driving_time_per_day = 2 * 20 / 60 # in hours
    total_driving_time_required = 50
    school_days_required = total_driving_time_required / driving_time_per_day
    result = school_days_required
    return result

print(solution())