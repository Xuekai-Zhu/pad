def solution():
    initial_money = 20
    snacks_cost = initial_money / 5
    remaining_money = initial_money - snacks_cost
    necessities_cost = remaining_money * 3 / 4
    remaining_money -= necessities_cost
    result = remaining_money
    return result

print(solution())