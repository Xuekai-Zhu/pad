def solution():
    
    total_snakes = 200
    num_boa_constrictors = 40
    num_pythons = 3 * num_boa_constrictors
    num_rattlesnakes = total_snakes - num_boa_constrictors - num_pythons
    result = num_rattlesnakes
    return result

print(solution())