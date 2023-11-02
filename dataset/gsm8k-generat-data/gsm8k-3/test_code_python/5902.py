def solution():
    """Kennedy grew tomatoes from three plants she had in her backyard.  The first tomato plant produced two dozen tomatoes.  The second plant produced 5 more than half as many tomatoes as the first plant.  And the third plant produced two more tomatoes than the second plant.  How many tomatoes did the three plants produce?"""
    # Calculate the number of tomatoes produced by the first plant
    plant1 = 2 * 12

    # Calculate the number of tomatoes produced by the second plant
    plant2 = int(0.5 * plant1 + 5)

    # Calculate the number of tomatoes produced by the third plant
    plant3 = plant2 + 2

    # Calculate the total number of tomatoes produced
    total_tomatoes = plant1 + plant2 + plant3

    # Display the total number of tomatoes
    result = total_tomatoes
    return result

print(solution())