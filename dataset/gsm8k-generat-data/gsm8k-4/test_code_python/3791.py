def solution():
    """Susan earned $600 from babysitting over the summer. She went shopping and spent half of it on clothes. Then she spent half of what was left on books. How much money did she have left?"""
    # Define the initial amount earned
    initial_amount = 600

    # Calculate the amount spent on clothes
    clothes_spent = initial_amount / 2

    # Calculate the amount left after buying clothes
    amount_left = initial_amount - clothes_spent

    # Calculate the amount spent on books
    books_spent = amount_left / 2

    # Calculate the amount left after buying books
    amount_left = amount_left - books_spent

    # return the result
    result = amount_left
    return result

print(solution())