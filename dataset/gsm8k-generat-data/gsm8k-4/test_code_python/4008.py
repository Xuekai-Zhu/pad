def solution():
    """Kris has been suspended for bullying many times. For every instance of bullying, she was suspended for 3 days. If she has been suspended for three times as many days as a typical person has fingers and toes, how many instances of bullying is she responsible for?"""
    # Define the number of fingers and toes a typical person has
    fingers_toes = 20

    # Calculate the total number of days Kris has been suspended for
    total_suspension_days = fingers_toes * 3

    # Calculate the number of instances of bullying Kris is responsible for
    instances_of_bullying = total_suspension_days / 3

    result = instances_of_bullying
    return result

print(solution())