def solution():
    """Nigel won $45 but gave some away. His mother gave him $80 more. If now Nigel has $10 more than twice the amount he originally had, how much money did he give away?"""
    # Define the initial amount Nigel won
    initial_amount = 45

    # Define the amount his mother gave him
    mother_amount = 80

    # Calculate the total amount Nigel has now
    total_amount = 2 * initial_amount + 10 + mother_amount

    # Calculate the amount Nigel gave away
    amount_given_away = initial_amount - (total_amount - initial_amount - mother_amount)

    # Display the amount Nigel gave away
    result = amount_given_away
    return result

print(solution())