def solution():
    """Asha has to buy some gifts but has no money. She decides to borrow $20 from her brother, $40 from her father, $30 from her mother and is gifted $70 by her granny. She adds this to her savings of $100 and goes out to Target to get what she wanted. If she spent 3/4 of the money, how much money did she remain with?"""
    borrowed_money = 20 + 40 + 30
    gifted_money = 70
    savings = 100
    total_money = borrowed_money + gifted_money + savings
    spent_money = total_money * (3/4)
    remaining_money = total_money - spent_money
    result = remaining_money
    return result

print(solution())