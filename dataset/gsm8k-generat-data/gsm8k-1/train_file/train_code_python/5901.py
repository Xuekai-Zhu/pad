def solution():
    """Kennedy grew tomatoes from three plants she had in her backyard. The first tomato plant produced two dozen tomatoes. The second plant produced 5 more than half as many tomatoes as the first plant. And the third plant produced two more tomatoes than the second plant. How many tomatoes did the three plants produce?"""
    first_plant = 2 * 12
    second_plant = 5 + (1/2 * first_plant)
    third_plant = second_plant + 2
    total_tomatoes = first_plant + second_plant + third_plant
    result = total_tomatoes
    return result

print(solution())