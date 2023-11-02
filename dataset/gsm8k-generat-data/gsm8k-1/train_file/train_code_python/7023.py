def solution():
    """Vicente bought 5 kilograms of rice and 3 pounds of meat. Each kilogram of rice is $2 and a pound of meat is $5. How much did Vicente spend in total?"""
    rice_weight = 5 # in kilograms
    rice_price_per_kg = 2 # in dollars
    rice_cost = rice_weight * rice_price_per_kg

    meat_weight = 3 # in pounds
    meat_price_per_pound = 5 # in dollars
    meat_cost = meat_weight * meat_price_per_pound

    total_cost = rice_cost + meat_cost
    result = total_cost
    return result

print(solution())