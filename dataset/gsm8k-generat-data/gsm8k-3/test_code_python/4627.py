def solution():
    """Asha has to buy some gifts but has no money. She decides to borrow $20 from her brother, $40 from her father, $30 from her mother and is gifted $70 by her granny. She adds this to her savings of $100 and goes out to Target to get what she wanted. If she spent 3/4 of the money, how much money did she remain with?"""
    # Calculate the total amount of money Asha had to spend
    total_money = 20 + 40 + 30 + 70 + 100

    # Calculate the amount of money Asha spent
    spent_money = total_money * 3/4

    # Calculate the amount of money Asha remained with
    remained_money = total_money - spent_money

    # Display the amount of money Asha remained with
    result = remained_money
    return result

print(solution())