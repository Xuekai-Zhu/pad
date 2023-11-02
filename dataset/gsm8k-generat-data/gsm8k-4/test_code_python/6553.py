def solution():
    """Elois needs 4 bananas to make 1 loaf of banana bread. On Monday, she makes 3 loaves of banana bread. On Tuesday, she makes twice as many loaves of banana bread as Monday. How many bananas did she use to make all the banana bread?"""
    # Define the number of bananas needed for each loaf of banana bread
    bananas_per_loaf = 4

    # Calculate the total number of loaves of banana bread made
    monday_banana_bread = 3
    tuesday_banana_bread = monday_banana_bread * 2
    total_banana_bread = monday_banana_bread + tuesday_banana_bread

    # Calculate the total number of bananas used
    total_bananas = total_banana_bread * bananas_per_loaf

    # return the result
    result = total_bananas
    return result

print(solution())