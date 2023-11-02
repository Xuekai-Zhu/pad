def solution():
    
    initial_balloons = 12
    final_balloons = 50
    balloons_added = final_balloons - initial_balloons
    rate = 2 / 5  
    time = balloons_added / rate
    result = time
    return result

print(solution())