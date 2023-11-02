def solution():
    """Kennedy grew tomatoes from three plants she had in her backyard. The first tomato plant produced two dozen tomatoes. The second plant produced 5 more than half as many tomatoes as the first plant. And the third plant produced two more tomatoes than the second plant. How many tomatoes did the three plants produce?"""
    # Define the number of tomatoes produced by the first plant
    first_plant = 2 * 12

    # Define the number of tomatoes produced by the second plant
    second_plant = (0.5 * first_plant) + 5

    # Define the number of tomatoes produced by the third plant
    third_plant = second_plant + 2

    # Calculate the total number of tomatoes produced
    total_tomatoes = first_plant + second_plant + third_plant

    # return the result
    result = total_tomatoes
    return result

print(solution())