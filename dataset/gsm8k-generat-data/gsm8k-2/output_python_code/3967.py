def solution():
    """Linda was gathering eggs from her chicken coops. When she was done, she had three times as many white eggs as brown eggs. On her way back to the house, she stumbled, dropping her egg basket. Upon inspecting the damage, she found that all 5 of the brown eggs survived, but now she only had a dozen eggs left. How many eggs did Linda break?"""
    # Let's assume the number of brown eggs is "b"
    b = 5
    w = 3 * b  # Since Linda had 3 times as many white eggs as brown eggs
    total_eggs = b + w
    broken_eggs = total_eggs - 12  # Since Linda was left with only 12 eggs after the accident
    result = broken_eggs
    return result

print(solution())