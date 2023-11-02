def solution():
    
    total_money = 10000
    natalie_share = total_money / 2
    remaining_money = total_money - natalie_share
    rick_share = remaining_money * 0.6
    lucy_share = total_money - natalie_share - rick_share
    result = lucy_share
    return result

print(solution())