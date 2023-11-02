def solution():
    """Tom went to the store to buy fruit. Lemons cost $2, papayas cost $1, and mangos cost $4. For every 4 fruits that customers buy, the store offers a $1 discount. Tom buys 6 lemons, 4 papayas, and 2 mangos. How much will he pay?"""
    # Define the prices of lemons, papayas, and mangos
    LEMON_PRICE = 2
    PAPAYA_PRICE = 1
    MANGO_PRICE = 4

    # Define the quantities of fruits that Tom buys
    lemon_qty = 6
    papaya_qty = 4
    mango_qty = 2

    # Calculate the total cost before discount
    total_cost = (LEMON_PRICE * lemon_qty) + (PAPAYA_PRICE * papaya_qty) + (MANGO_PRICE * mango_qty)

    # Calculate the number of sets of 4 fruits Tom buys
    sets_of_4 = (lemon_qty + papaya_qty + mango_qty) // 4

    # Calculate the discount Tom gets
    discount = sets_of_4 * 1

    # Calculate the total cost after discount
    total_cost -= discount
    
    result = total_cost
    return result

print(solution())