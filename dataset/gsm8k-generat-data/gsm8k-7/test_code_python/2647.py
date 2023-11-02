def solution():
    total_snakes = 200
    num_boa_constrictors = 40

    # Calculate the number of pythons
    num_pythons = num_boa_constrictors * 3

    # Calculate the number of rattlesnakes
    num_rattlesnakes = total_snakes - num_boa_constrictors - num_pythons

    result = num_rattlesnakes
    return result

print(solution())