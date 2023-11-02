def solution():
    
    cans = 144
    newspapers = 20
    cans_money = (cans // 12) * 0.5
    newspaper_money = (newspapers // 5) * 1.5
    total_money = cans_money + newspaper_money
    result = total_money
    return result

print(solution())