def solution():
    """Kris has been suspended for bullying many times.  For every instance of bullying, she was suspended for 3 days.  If she has been suspended for three times as many days as a typical person has fingers and toes, how many instances of bullying is she responsible for?"""
    # Define the number of fingers and toes in a typical person
    FINGERS_TOES = 20

    # Calculate the total number of suspension days
    suspension_days = FINGERS_TOES * 3 * 3

    # Calculate the number of instances of bullying
    bullying_instances = suspension_days / 3

    # Display the number of instances of bullying
    result = bullying_instances
    return result

print(solution())