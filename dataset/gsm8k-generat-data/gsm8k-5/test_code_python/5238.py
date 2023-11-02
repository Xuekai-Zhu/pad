def solution():
    cans = 144
    newspapers = 20
    
    # Calculate the money received for recycling cans
    cans_money = (cans // 12) * 0.5
    
    # Calculate the money received for recycling newspapers
    newspaper_money = (newspapers // 5) * 1.5
    
    # Calculate the total money received
    total_money = cans_money + newspaper_money
    result = total_money
    return result

print(solution())