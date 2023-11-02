def solution():
    """Jangshe spent $610 on 7 pieces of clothing. One piece was $49 and another piece was $81. If the other pieces were all the same price, how many dollars was one of the other pieces?"""
    # Define the total cost and the prices of two of the pieces of clothing
    total_cost = 610
    price1 = 49
    price2 = 81

    # Calculate the sum of the prices of the two known pieces of clothing
    sum_prices = price1 + price2

    # Calculate the cost of the other 5 pieces of clothing
    cost_others = total_cost - sum_prices

    # Calculate the price of one of the other pieces of clothing
    price_other = cost_others / 5

    result = price_other
    return result

print(solution())