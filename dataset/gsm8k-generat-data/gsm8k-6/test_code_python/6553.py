def solution():
    # Calculate the total number of bananas used to make banana bread
    bananas_for_one_loaf = 4
    monday_loaves = 3
    tuesday_loaves = 2 * monday_loaves
    total_loaves = monday_loaves + tuesday_loaves
    total_bananas = total_loaves * bananas_for_one_loaf
    result = total_bananas
    return result

print(solution())