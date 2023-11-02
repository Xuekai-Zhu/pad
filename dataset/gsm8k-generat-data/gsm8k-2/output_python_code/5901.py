def solution():
    """Kennedy grew tomatoes from three plants she had in her backyard. The first tomato plant produced two dozen tomatoes. The second plant produced 5 more than half as many tomatoes as the first plant. And the third plant produced two more tomatoes than the second plant. How many tomatoes did the three plants produce?"""
    first_plant_tomatoes = 24
    second_plant_tomatoes = (0.5 * first_plant_tomatoes) + 5
    third_plant_tomatoes = second_plant_tomatoes + 2
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + third_plant_tomatoes
    result = total_tomatoes
    return result

print(solution())