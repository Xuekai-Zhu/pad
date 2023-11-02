def solution():
    # Calculate the total time Jessica spends driving to and from school each day
    daily_time = 2 * (20/60)  # 20 minutes to drive to school, and 20 minutes to drive back

    # Calculate the number of school days it will take Jessica to reach 50 hours of driving time
    total_days = 50 / daily_time
    
    result = total_days
    return result

print(solution())