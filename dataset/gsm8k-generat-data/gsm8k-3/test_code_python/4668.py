def solution():
    """Each week, Paul has 2 hours of homework on weeknights and 5 hours for the entire weekend. This week Paul has practice 2 nights out of the week and can't do any homework those nights. How many hours of homework does he have to average for the other nights to get his week's homework done?"""
    # Define the total amount of homework Paul needs to complete
    total_homework = 2 * 5 + 2 * 2

    # Define the number of homework days Paul has left
    homework_days_left = 7 - 2  # deduct 2 practice nights

    # Calculate the number of hours of homework Paul has to do each night
    homework_hours_per_night = (total_homework / homework_days_left)

    # Display the number of hours of homework Paul has to do each night
    result = homework_hours_per_night
    return result

print(solution())