def solution():
    
    plant1_tomatoes = 8
    plant2_tomatoes = plant1_tomatoes + 4
    combined_tomatoes = plant1_tomatoes + plant2_tomatoes
    plant3_tomatoes = 3 * combined_tomatoes
    plant4_tomatoes = 3 * combined_tomatoes
    total_tomatoes = plant1_tomatoes + plant2_tomatoes + plant3_tomatoes + plant4_tomatoes
    result = total_tomatoes
    return result

print(solution())