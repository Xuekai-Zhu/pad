def solution():
    """Each week, Paul has 2 hours of homework on weeknights and 5 hours for the entire weekend. This week Paul has practice 2 nights out of the week and can't do any homework those nights. How many hours of homework does he have to average for the other nights to get his week's homework done?"""
    total_homework_hours = 2 * 5 # 10 hours of homework for the week
    nights_without_homework = 2
    remaining_nights = 7 - nights_without_homework - 2 # 3 nights left for homework
    homework_hours_per_night = (total_homework_hours - 5 - 4) / remaining_nights
    result = homework_hours_per_night
    return result

print(solution())