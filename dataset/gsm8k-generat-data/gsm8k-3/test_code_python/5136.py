def solution():
    """Mario has 3 hibiscus plants in his garden.  The first hibiscus plant has 2 flowers.  The second hibiscus plant has twice as many flowers as the first hibiscus plant.  The third hibiscus plant has four times as many flowers as the second hibiscus plant.  How many total blossoms does Mario have?"""
    
    # Define the number of flowers for each hibiscus plant
    plant1_flowers = 2
    plant2_flowers = 2 * plant1_flowers
    plant3_flowers = 4 * plant2_flowers

    # Calculate the total number of flowers
    total_blossoms = plant1_flowers + plant2_flowers + plant3_flowers

    # Display the total number of blossoms
    result = total_blossoms
    return result

print(solution())