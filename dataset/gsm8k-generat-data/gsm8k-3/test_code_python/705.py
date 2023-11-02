def solution():
    """Isabel has some money in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. If she has $51 left, how much money, in dollars, did she have at first?"""
    # Define the amount of money Isabel has left
    remaining_money = 51

    # Work backwards to find the amount of money Isabel started with
    brother_book_cost = remaining_money * 2
    remaining_money += brother_book_cost
    toy_cost = remaining_money * 2
    remaining_money += toy_cost

    # Display the amount of money Isabel started with
    result = remaining_money
    return result

print(solution())