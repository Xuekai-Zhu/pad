def solution():
    morning_coffee_price = 3.0
    afternoon_coffee_price = 2.5
    num_coffees_per_day = 2
    num_days = 20

    # Calculate the total cost of morning coffees over 20 days
    total_morning_coffee_cost = morning_coffee_price * num_coffees_per_day * num_days

    # Calculate the total cost of afternoon coffees over 20 days
    total_afternoon_coffee_cost = afternoon_coffee_price * num_coffees_per_day * num_days

    # Calculate the total cost of all coffees over 20 days
    total_cost = total_morning_coffee_cost + total_afternoon_coffee_cost
    result = total_cost
    return result

print(solution())