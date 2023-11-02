def solution():
    old_coffee_price = 2
    new_coffee_price = old_coffee_price * 1.5
    old_coffees_bought = 4
    new_coffees_bought = old_coffees_bought / 2
    old_daily_spend = old_coffee_price * old_coffees_bought
    new_daily_spend = new_coffee_price * new_coffees_bought
    daily_savings = old_daily_spend - new_daily_spend
    result = daily_savings
    return result

print(solution())