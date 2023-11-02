def solution():
    """Evan’s dog weighs 63 pounds; it weighs 7 times as much as Ivan’s dog.  Together, what is the weight of the dogs?"""
    # Define the weight of Evan's dog and the weight ratio between Evan's dog and Ivan's dog
    EVAN_WEIGHT = 63
    RATIO = 7

    # Calculate the weight of Ivan's dog
    ivan_weight = EVAN_WEIGHT // RATIO

    # Calculate the total weight of the two dogs
    total_weight = EVAN_WEIGHT + ivan_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())