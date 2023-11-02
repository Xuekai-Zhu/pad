def solution():
    """Jane is shopping for some fruit. She sees a stand of fruit advertising 10 apples for $2, and another one advertising 5 oranges for $1.50. Assuming there's no price discount for buying in bulk, how much would Jane spend in cents if she bought 12 of the cheaper of the two fruits?"""
    # Calculate the price of 12 apples and 12 oranges
    apples_price = 2 * (12 // 10) + 2 * (12 % 10)
    oranges_price = 1.5 * (12 // 5) + 1.5 * (12 % 5)

    # Determine which fruit is cheaper and calculate Jane's total cost
    if apples_price < oranges_price:
        total_cost = apples_price
    else:
        total_cost = oranges_price

    # Convert the total cost to cents and return the result
    result = total_cost * 100
    return result

print(solution())