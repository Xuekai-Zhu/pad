def solution():
    total_money = 10000
    Natalie_money = total_money / 2
    remaining_money = total_money - Natalie_money
    Rick_money = remaining_money * 0.6
    Lucy_money = remaining_money - Rick_money
    result = Lucy_money
    return result

print(solution())