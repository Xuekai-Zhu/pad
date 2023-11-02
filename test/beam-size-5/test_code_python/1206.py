def solution():
    
    packs_of_balloons = 10
    balloons_per_pack = 30
    total_balloons = packs_of_balloons * balloons_per_pack
    balloons_left = 12
    balloons_thrown = total_balloons - balloons_left
    result = balloons_thrown
    return result

print(solution())