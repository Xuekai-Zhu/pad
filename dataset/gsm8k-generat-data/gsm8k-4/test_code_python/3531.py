def solution():
    """Nigel won $45 but gave some away. His mother gave him $80 more. If now Nigel has $10 more than twice the amount he originally had, how much money did he give away?"""
    # Define the amount Nigel won
    initial_amount = 45

    # Define the amount Nigel's mother gave him
    mother_amount = 80

    # Calculate Nigel's current amount
    current_amount = initial_amount + mother_amount

    # Calculate twice the amount Nigel originally had
    twice_initial_amount = initial_amount * 2

    # Calculate the amount Nigel gave away
    given_away = current_amount - twice_initial_amount - 10

    # return the result
    result = given_away
    return result

print(solution())