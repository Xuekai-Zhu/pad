def solution():
    num_weekdays = 5
    num_club_days = 3
    num_days = 7
    total_shirts_per_week = (num_weekdays + num_club_days + 2)  # 2 for Saturday and Sunday
    shirts_per_two_weeks = total_shirts_per_week * 2  # laundry once every two weeks
    result = shirts_per_two_weeks
    return result

print(solution())