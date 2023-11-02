def solution():
    """Renaldo drove 15 kilometers. Ernesto drove 7 kilometers more than one-third of Renaldo's distance. How many kilometers did the 2 men drive in total?"""
    # Define the distance Renaldo drove
    renaldo_distance = 15

    # Calculate the distance Ernesto drove
    ernesto_distance = (1/3) * renaldo_distance + 7

    # Calculate the total distance the two men drove
    total_distance = renaldo_distance + ernesto_distance

    result = total_distance
    return result

print(solution())