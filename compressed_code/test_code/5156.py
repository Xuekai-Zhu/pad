def solution():
    
    starting_money = 9
    allowance = 5
    frisbee_cost = 4
    puzzle_cost = 3
    birthday_money = 8
    total_spent = frisbee_cost + puzzle_cost
    total_money = starting_money + allowance + birthday_money - total_spent
    result = total_money
    return result

print(solution())