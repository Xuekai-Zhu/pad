def solution():
    
    total_money = 48
    ryan_share = total_money * (2/3)
    ryan_remaining = ryan_share - 10 + 7
    leo_remaining = total_money - ryan_remaining
    result = leo_remaining
    return result

print(solution())