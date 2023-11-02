def solution():
    """Mabel planted 4 tomato plants. One tomato plant bore 8 tomatoes and another bore 4 more tomatoes than the first. The two remaining plants each bore three times the number of tomatoes as the first two plants combined. How many tomatoes does Mabel have?"""
    plant1 = 8
    plant2 = 8 + 4
    plant3 = 3 * (plant1 + plant2)
    plant4 = 3 * (plant1 + plant2)
    total_tomatoes = plant1 + plant2 + plant3 + plant4
    result = total_tomatoes
    return result

print(solution())