def solution():
    """Each week, Paul has 2 hours of homework on weeknights and 5 hours for the entire weekend.
    This week Paul has practice 2 nights out of the week and can't do any homework those nights.
    How many hours of homework does he have to average for the other nights to get his week's homework done?"""
    # Define the total amount of homework for the week
    total_homework = 2 * 5 + 5

    # Define the number of nights available for homework
    available_nights = 7 - 2

    # Calculate the remaining amount of homework
    remaining_homework = total_homework - (2 * 2)

    # Divide the remaining homework by the number of available nights
    average_homework = remaining_homework / available_nights
    
    result = average_homework
    return result

print(solution())