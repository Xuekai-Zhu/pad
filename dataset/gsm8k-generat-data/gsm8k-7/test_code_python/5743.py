def solution():
    old_plan_price = 150
    increase_percentage = 0.3  # 30% increase

    # Calculate the increase in price
    price_increase = old_plan_price * increase_percentage

    # Calculate the new plan price
    new_plan_price = old_plan_price + price_increase
    result = new_plan_price
    return result

print(solution())