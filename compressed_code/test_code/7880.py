def solution():
    
    total_snakes = 200
    boa_constrictors = 40
    pythons = 3 * boa_constrictors
    rattlesnakes = total_snakes - (boa_constrictors + pythons)
    result = rattlesnakes
    return result

print(solution())