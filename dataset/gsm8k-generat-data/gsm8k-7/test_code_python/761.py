def solution():
    total_budget = 60
    hummus_price = 5
    num_hummus_containers = 2

    chicken_price = 20
    bacon_price = 10
    veggie_price = 10

    remaining_budget = total_budget - (hummus_price * num_hummus_containers) - chicken_price - bacon_price - veggie_price

    apple_price = 2
    num_apples = remaining_budget // apple_price
    result = num_apples
    return result

print(solution())