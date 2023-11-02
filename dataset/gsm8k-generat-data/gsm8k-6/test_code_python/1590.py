def solution():
    # Calculate the original daily cost of coffee for John
    original_cost = 4 * 2  # John buys 4 coffees for $2 each
    
    # Calculate the new daily cost of coffee for John
    new_price = 2 * 1.5  # The price increased by 50%
    new_quantity = 4 / 2  # John now buys half the amount of coffee
    new_cost = new_price * new_quantity
    
    # Calculate how much money John saves per day compared to what he used to spend
    savings = original_cost - new_cost
    result = savings
    return result

print(solution())