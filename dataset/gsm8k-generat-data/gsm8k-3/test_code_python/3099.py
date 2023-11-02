def solution():
    """Natasha exercised for 30 minutes every day for one week. Esteban exercised for 10 minutes on each of nine days. How many hours did Natasha and Esteban exercise in total?"""
    # Define the number of days for each person
    NATASHA_DAYS = 7
    ESTEBAN_DAYS = 9

    # Define the length of exercise for each person
    NATASHA_LENGTH = 0.5  # 30 minutes
    ESTEBAN_LENGTH = 0.17  # 10 minutes

    # Calculate the total exercise time for each person
    natasha_total = NATASHA_DAYS * NATASHA_LENGTH
    esteban_total = ESTEBAN_DAYS * ESTEBAN_LENGTH

    # Calculate the total exercise time for both people
    total_time = natasha_total + esteban_total

    # Convert the total time to hours
    total_time_hours = total_time / 2

    # Display the total exercise time
    result = total_time_hours
    return result

print(solution())