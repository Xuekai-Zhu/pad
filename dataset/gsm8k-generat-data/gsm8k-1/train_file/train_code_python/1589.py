def solution():
    """John used to buy 4 coffees a day for $2 each. They raised the price by 50% so he cut the number of coffees he drinks in half. How much money does he save per day compared to what he used to spend?"""
    original_price = 2
    raised_price = original_price * 1.5
    original_coffees = 4
    new_coffees = original_coffees / 2
    original_total_cost = original_price * original_coffees
    new_total_cost = raised_price * new_coffees
    savings = original_total_cost - new_total_cost
    result = savings
    return result

print(solution())