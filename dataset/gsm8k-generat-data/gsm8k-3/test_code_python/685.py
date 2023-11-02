def solution():
    """There are some kids in camp. Half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning. 750 kids are going to soccer camp in the afternoon. How many kids there in camp altogether?"""
    # Let's define the number of kids in camp as x
    # Half of the kids are going to soccer camp, so 0.5x are going to soccer camp
    # 1/4 of the kids going to soccer camp are going to soccer camp in the morning, so (0.5x * 0.25) = 0.125x are going to soccer camp in the morning
    # 750 kids are going to soccer camp in the afternoon, so 0.5x - 0.125x = 750
    # Simplifying the equation, we get 0.375x = 750
    # Solving for x, we get x = 2000
    # Therefore, there are 2000 kids in camp altogether

    total_kids = 2000
    result = total_kids
    return result

print(solution())