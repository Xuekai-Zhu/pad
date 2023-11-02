def solution():
    
    starting_money = 21
    doris_spent = 6
    martha_spent = doris_spent / 2
    remaining_money = starting_money - doris_spent - martha_spent
    result = remaining_money
    return result

print(solution())