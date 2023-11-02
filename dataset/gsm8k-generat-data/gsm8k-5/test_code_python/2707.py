def solution():
    # Renaldo drove 15 kilometers
    renaldo_distance = 15

    # Ernesto drove 7 kilometers more than one-third of Renaldo's distance
    ernesto_distance = (1/3) * renaldo_distance + 7

    # Calculate the total distance the two men drove
    total_distance = renaldo_distance + ernesto_distance

    result = total_distance
    return result

print(solution())