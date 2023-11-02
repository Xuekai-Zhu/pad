def solution():
    scissors_cost = 5
    erasers_cost = 4
    total_cost = (scissors_cost * 8) + (erasers_cost * 10)
    initial_money = 100
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())