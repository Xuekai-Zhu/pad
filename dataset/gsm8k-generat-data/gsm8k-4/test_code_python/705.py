def solution():
    """Isabel has some money in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. If she has $51 left, how much money, in dollars, did she have at first?"""
    # Define the initial amount of money
    initial_money = None
    
    # Calculate the amount of money spent on the toy
    toy_cost = initial_money / 2

    # Calculate the remaining amount of money
    remaining_money = initial_money - toy_cost

    # Calculate the amount of money spent on the book
    book_cost = remaining_money / 2

    # Calculate the final amount of money
    final_money = remaining_money - book_cost

    # The final_money is given as $51, so we can solve for initial_money
    initial_money = final_money + book_cost + remaining_money + toy_cost

    # Return the result
    result = initial_money
    return result

print(solution())