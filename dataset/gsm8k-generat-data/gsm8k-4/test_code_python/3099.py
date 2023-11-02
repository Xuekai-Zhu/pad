def solution():
    """Natasha exercised for 30 minutes every day for one week. Esteban exercised for 10 minutes on each of nine days. How many hours did Natasha and Esteban exercise in total?"""
    # Define the number of days and minutes for each person
    NATASHA_DAYS = 7
    NATASHA_MINUTES = 30
    ESTEBAN_DAYS = 9
    ESTEBAN_MINUTES = 10

    # Calculate the total minutes for each person
    natasha_total_minutes = NATASHA_DAYS * NATASHA_MINUTES
    esteban_total_minutes = ESTEBAN_DAYS * ESTEBAN_MINUTES

    # Convert the minutes to hours
    natasha_hours = natasha_total_minutes / 60
    esteban_hours = esteban_total_minutes / 60

    # Calculate the total hours
    total_hours = natasha_hours + esteban_hours

    # Return the result
    result = total_hours
    return result

print(solution())