def solution():
    
    total_money = 10000
    natalie_money = total_money * 0.5
    remaining_money = total_money - natalie_money
    rick_money = remaining_money * 0.6
    lucy_money = total_money - natalie_money - rick_money
    result = lucy_money
    return result

print(solution())