def solution():
    servings_per_bottle = 6
    half_bottle_per_day = 0.5
    num_days = 14
    sale_price_per_bottle = 3.0

    # Calculate the total number of servings Tricia will drink in 2 weeks
    total_servings = servings_per_bottle * half_bottle_per_day * num_days

    # Calculate the total number of bottles Tricia needs to buy
    total_bottles = total_servings / servings_per_bottle

    # Calculate the total cost of all bottles of iced coffee that Tricia needs to buy
    total_cost = total_bottles * sale_price_per_bottle
    result = total_cost
    return result

print(solution())