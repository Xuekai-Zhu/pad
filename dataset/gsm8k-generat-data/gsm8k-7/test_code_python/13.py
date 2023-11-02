def solution():
    cheddar_amount = 2
    cheddar_price = 10

    cream_price = cheddar_price / 2

    cold_cuts_price = cheddar_price * 2

    # Calculate the total cost of all ingredients
    total_cost = (cheddar_amount * cheddar_price) + cream_price + cold_cuts_price
    result = total_cost
    return result

print(solution())