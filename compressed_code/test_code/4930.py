def solution():
    
    first_six_days = 100 * 6
    last_day = 2 * (100 * 6)

    total_visitors = first_six_days + last_day
    earnings = total_visitors * 0.01
    result = earnings
    return result

print(solution())