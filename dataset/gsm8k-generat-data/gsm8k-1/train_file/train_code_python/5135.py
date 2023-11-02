def solution():
    """Mario has 3 hibiscus plants in his garden. The first hibiscus plant has 2 flowers. The second hibiscus plant has twice as many flowers as the first hibiscus plant. The third hibiscus plant has four times as many flowers as the second hibiscus plant. How many total blossoms does Mario have?"""
    plant_1_flowers = 2
    plant_2_flowers = plant_1_flowers * 2
    plant_3_flowers = plant_2_flowers * 4
    total_blossoms = plant_1_flowers + plant_2_flowers + plant_3_flowers
    result = total_blossoms
    return result

print(solution())