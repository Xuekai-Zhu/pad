def solution():
    """Nancy buys 2 coffees a day. She grabs a double espresso for $3.00 every morning. In the afternoon, she grabs an iced coffee for $2.50. After 20 days, how much money has she spent on coffee?"""
    double_espresso_price = 3
    iced_coffee_price = 2.5
    days = 20
    total_coffees = 2 * days
    total_cost = (double_espresso_price + iced_coffee_price) * total_coffees
    result = total_cost
    return result

print(solution())