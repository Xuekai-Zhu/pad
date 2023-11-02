def solution():
    """Josh has some money. He spent $1.75 on a drink, and then spent another $1.25. If he had $6 left, how much money, in dollars, did Josh have at first?"""
    # Define the amount Josh spent on his first purchase and his second purchase
    purchase_1 = 1.75
    purchase_2 = 1.25

    # Define the amount of money Josh had left after his purchases
    remaining_money = 6

    # Calculate the total amount of money Josh had at first
    total_money = remaining_money + purchase_1 + purchase_2

    # Display the total amount of money Josh had at first
    result = total_money
    return result

print(solution())