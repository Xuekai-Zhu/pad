def solution():
    """Tina buys a loaf of bread for $50, 2oz of ham for $150, and a cake for $200. What percent of the cost is the ham and bread?"""
    # Define the prices of each item
    bread_price = 50
    ham_price = 150
    cake_price = 200

    # Calculate the total cost
    total_cost = bread_price + ham_price + cake_price

    # Calculate the cost of the ham and bread
    hb_cost = bread_price + ham_price

    # Calculate the percentage of the cost that is the ham and bread
    hb_percent = (hb_cost / total_cost) * 100

    # return the result
    result = hb_percent
    return result

print(solution())