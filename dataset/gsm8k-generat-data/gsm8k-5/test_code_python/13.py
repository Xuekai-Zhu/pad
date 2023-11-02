def solution():
    cheddar_price = 10  # Jasper buys 2 pounds of cheddar cheese for $10
    cream_cheese_price = cheddar_price / 2  # The cream cheese costs half the price of the cheddar cheese
    cold_cuts_price = cheddar_price * 2  # The cold cuts cost twice the price of the cheddar cheese

    # Calculate the total cost of the ingredients
    total_cost = (2 * cheddar_price) + cream_cheese_price + cold_cuts_price
    result = total_cost
    return result

print(solution())