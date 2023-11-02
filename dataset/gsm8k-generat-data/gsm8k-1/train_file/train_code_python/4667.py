def solution():
    """Each week, Paul has 2 hours of homework on weeknights and 5 hours for the entire weekend. This week Paul has practice 2 nights out of the week and can't do any homework those nights. How many hours of homework does he have to average for the other nights to get his week's homework done?"""
    weeknight_hours = 2
    weekend_hours = 5
    nights_without_homework = 2
    remaining_days = 7 - nights_without_homework - 2
    total_homework_hours = weeknight_hours * remaining_days + weekend_hours
    average_homework_hours = total_homework_hours / remaining_days
    result = average_homework_hours
    return result

print(solution())