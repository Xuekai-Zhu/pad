def solution():
    """Linda was gathering eggs from her chicken coops. When she was done, she had three times as many white eggs as brown eggs. On her way back to the house, she stumbled, dropping her egg basket. Upon inspecting the damage, she found that all 5 of the brown eggs survived, but now she only had a dozen eggs left. How many eggs did Linda break?"""
    # Define the initial ratio of white to brown eggs
    white_to_brown_ratio = 3

    # Calculate the number of brown eggs
    brown_eggs = 5

    # Calculate the number of white eggs
    white_eggs = brown_eggs * white_to_brown_ratio

    # Calculate the total number of eggs before the accident
    total_eggs_before = brown_eggs + white_eggs

    # Calculate the number of eggs that were broken
    broken_eggs = total_eggs_before - 12

    # return the result
    result = broken_eggs
    return result

print(solution())