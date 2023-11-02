def solution():
    """John used to buy 4 coffees a day for $2 each. They raised the price by 50% so he cut the number of coffees he drinks in half. How much money does he save per day compared to what he used to spend?"""
    old_price = 2
    new_price = old_price * 1.5
    old_quantity = 4
    new_quantity = old_quantity / 2
    old_spending = old_quantity * old_price
    new_spending = new_quantity * new_price
    savings = old_spending - new_spending
    result = savings
    return result

print(solution())