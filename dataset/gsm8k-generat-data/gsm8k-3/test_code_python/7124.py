def solution():
    """Due to the restrictions of Coronavirus, Mr. Trent, the local store owner, increased the prices of goods at his store by 15% each to make the same income he was making before. If buying an orange was $40 and the price of purchasing a mango was $50, calculate how much it costs in total now to buy ten oranges and ten mangoes at the new prices."""
    # Define the original prices of an orange and a mango
    ORANGE_PRICE = 40
    MANGO_PRICE = 50

    # Define the percentage increase in prices
    PRICE_INCREASE_PERCENTAGE = 15

    # Calculate the new prices of an orange and a mango
    new_orange_price = ORANGE_PRICE * (1 + PRICE_INCREASE_PERCENTAGE/100)
    new_mango_price = MANGO_PRICE * (1 + PRICE_INCREASE_PERCENTAGE/100)

    # Calculate the total cost of buying 10 oranges and 10 mangoes at the new prices
    total_cost = 10 * new_orange_price + 10 * new_mango_price

    # Display the total cost
    result = total_cost
    return result

print(solution())