def solution():
    
    goal = 150
    money_from_first_group = 10 * 3
    money_from_second_group = 5 * 15
    total_money_so_far = money_from_first_group + money_from_second_group
    remaining_money = goal - total_money_so_far
    result = remaining_money
    return result

print(solution())