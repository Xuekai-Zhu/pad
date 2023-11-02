def solution():
    """Asha has to buy some gifts but has no money. She decides to borrow $20 from her brother, $40 from her father, $30 from her mother and is gifted $70 by her granny. She adds this to her savings of $100 and goes out to Target to get what she wanted. If she spent 3/4 of the money, how much money did she remain with?"""
    # Define the amounts borrowed and gifted, and the savings
    borrowed_1 = 20
    borrowed_2 = 40
    borrowed_3 = 30
    gifted = 70
    savings = 100

    # Calculate the total amount of money available
    total_money = borrowed_1 + borrowed_2 + borrowed_3 + gifted + savings

    # Calculate how much money was spent
    spent = total_money * (3/4)

    # Calculate how much money is remaining
    remaining = total_money - spent

    # return the result
    result = remaining
    return result

print(solution())