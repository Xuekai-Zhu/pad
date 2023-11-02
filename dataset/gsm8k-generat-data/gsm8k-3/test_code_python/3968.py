def solution():
    """Linda was gathering eggs from her chicken coops. When she was done, she had three times as many white eggs as brown eggs. On her way back to the house, she stumbled, dropping her egg basket. Upon inspecting the damage, she found that all 5 of the brown eggs survived, but now she only had a dozen eggs left. How many eggs did Linda break?"""
    # Let x be the number of brown eggs Linda gathered
    x = 5

    # Let y be the number of white eggs Linda gathered
    y = 3*x

    # Let z be the total number of eggs Linda gathered
    z = x + y

    # Let a be the number of eggs Linda broke
    a = z - 12

    # Display the number of eggs Linda broke
    result = a
    return result

print(solution())