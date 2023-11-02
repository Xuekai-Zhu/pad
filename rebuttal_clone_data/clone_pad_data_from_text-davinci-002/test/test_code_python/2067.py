def solution():
    tea_servings = 2
    per_serving = 1
    total_servings = tea_servings * per_serving
    size_of_container = 16
    number_of_servings_in_container = 6
    total_number_of_servings = size_of_container * number_of_servings_in_container
    result = total_number_of_servings / total_servings
    return result

print(solution())