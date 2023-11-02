def solution():
    yanni_initial = 85
    yanni_mother = 40
    yanni_found = 50
    toy_cost = 160
    total_money = yanni_initial + yanni_mother + yanni_found
    money_left = total_money - toy_cost
    result = money_left
    
    return result

print(solution())