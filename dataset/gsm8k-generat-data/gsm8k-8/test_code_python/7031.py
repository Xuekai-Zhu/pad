def solution():
    total_money = 600
    gas_spending = total_money / 3
    remaining_money = total_money - gas_spending
    food_spending = remaining_money / 4
    remaining_money = remaining_money - food_spending
    result = remaining_money
    return result

print(solution())