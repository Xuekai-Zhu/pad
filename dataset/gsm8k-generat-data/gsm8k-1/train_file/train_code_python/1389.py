def solution():
    """Nancy buys 2 coffees a day. She grabs a double espresso for $3.00 every morning. In the afternoon, she grabs an iced coffee for $2.50. After 20 days, how much money has she spent on coffee?"""
    espresso_price = 3.00
    iced_coffee_price = 2.50
    coffees_per_day = 2
    days = 20
    total_coffees = coffees_per_day * days
    total_cost = (espresso_price + iced_coffee_price) * total_coffees
    result = total_cost
    return result

print(solution())