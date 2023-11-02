def solution():
    """Tom went to the store to buy fruit. Lemons cost $2, papayas cost $1, and mangos cost $4. For every 4 fruits that customers buy, the store offers a $1 discount. Tom buys 6 lemons, 4 papayas, and 2 mangos. How much will he pay?"""
    lemon_price = 2
    papaya_price = 1
    mango_price = 4
    total_fruits = 6 + 4 + 2
    total_cost = (6 * lemon_price) + (4 * papaya_price) + (2 * mango_price)
    discount = (total_fruits // 4) * 1
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())