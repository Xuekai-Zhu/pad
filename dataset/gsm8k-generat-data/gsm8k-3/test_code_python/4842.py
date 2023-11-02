def solution():
    """Tom went to the store to buy fruit. Lemons cost $2, papayas cost $1, and mangos cost $4. For every 4 fruits that customers buy, the store offers a $1 discount. Tom buys 6 lemons, 4 papayas, and 2 mangos. How much will he pay?"""
    # Define the prices of each type of fruit
    LEMON_PRICE = 2
    PAPAYA_PRICE = 1
    MANGO_PRICE = 4

    # Define the number of each type of fruit Tom buys
    lemon_count = 6
    papaya_count = 4
    mango_count = 2

    # Calculate the total cost of the fruits before the discount
    total_cost = (LEMON_PRICE * lemon_count) + (PAPAYA_PRICE * papaya_count) + (MANGO_PRICE * mango_count)

    # Calculate the number of fruit sets that Tom buys (a set is 4 fruits)
    fruit_sets = (lemon_count + papaya_count + mango_count) // 4

    # Calculate the discount amount
    discount = fruit_sets * 1

    # Calculate the total cost after the discount
    total_cost -= discount

    # Display the total cost
    result = total_cost
    return result

print(solution())