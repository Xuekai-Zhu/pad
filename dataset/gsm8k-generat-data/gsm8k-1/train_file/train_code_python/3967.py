def solution():
    """Linda was gathering eggs from her chicken coops. When she was done, she had three times as many white eggs as brown eggs. On her way back to the house, she stumbled, dropping her egg basket. Upon inspecting the damage, she found that all 5 of the brown eggs survived, but now she only had a dozen eggs left. How many eggs did Linda break?"""
    brown_eggs = 5
    white_eggs = 3 * brown_eggs
    total_eggs = brown_eggs + white_eggs
    broken_eggs = total_eggs - 12
    result = broken_eggs
    return result

print(solution())