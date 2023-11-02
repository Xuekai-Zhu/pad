def solution():
    """Mabel planted 4 tomato plants. One tomato plant bore 8 tomatoes and another bore 4 more tomatoes than the first. The two remaining plants each bore three times the number of tomatoes as the first two plants combined. How many tomatoes does Mabel have?"""
    plant1_tomatoes = 8
    plant2_tomatoes = plant1_tomatoes + 4
    combined_tomatoes = plant1_tomatoes + plant2_tomatoes
    plant3_tomatoes = 3 * combined_tomatoes
    plant4_tomatoes = 3 * combined_tomatoes
    total_tomatoes = plant1_tomatoes + plant2_tomatoes + plant3_tomatoes + plant4_tomatoes
    result = total_tomatoes
    return result

print(solution())