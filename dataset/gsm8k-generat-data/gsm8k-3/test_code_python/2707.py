def solution():
    """Renaldo drove 15 kilometers. Ernesto drove 7 kilometers more than one-third of Renaldo's distance. How many kilometers did the 2 men drive in total?"""
    # Define the distance Renaldo drove
    Renaldo_distance = 15

    # Calculate the distance Ernesto drove
    Ernesto_distance = (1/3) * Renaldo_distance + 7

    # Calculate the total distance
    total_distance = Renaldo_distance + Ernesto_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())