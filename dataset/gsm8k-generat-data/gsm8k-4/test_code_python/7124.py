def solution():
    """Due to the restrictions of Coronavirus, Mr. Trent, the local store owner, increased the prices of goods at his store by 15% each to make the same income he was making before. If buying an orange was $40 and the price of purchasing a mango was $50, calculate how much it costs in total now to buy ten oranges and ten mangoes at the new prices."""
    # Define the original prices of oranges and mangoes
    orange_price = 40
    mango_price = 50

    # Calculate the new prices of oranges and mangoes after the price increase
    new_orange_price = orange_price * 1.15
    new_mango_price = mango_price * 1.15

    # Calculate the total cost of buying 10 oranges and 10 mangoes at the new prices
    total_cost = (new_orange_price * 10) + (new_mango_price * 10)

    # Return the result
    result = total_cost
    return result

print(solution())