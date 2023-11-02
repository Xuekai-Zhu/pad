def solution():
    # Define the number of gloves Randy has
    glove_count = 29

    # Set up an equation to solve for the number of bats
    # 1 = 7x - g, where x is the number of bats and g is the number of gloves
    bat_count = (glove_count - 1) / 7

    result = bat_count
    return result

print(solution())