def solution():
    combined_height = 92
    tamara_height = 0
    kim_height = 0

    # Set up the equation system to solve for Tamara and Kim's height
    # Tamara = 3 * Kim - 4  and  Tamara + Kim = combined_height
    # Substitute Tamara's height equation into the combined height equation to get: 3 * Kim - 4 + Kim = combined_height
    # Simplify to get: 4 * Kim = combined_height + 4
    # Solve for Kim's height to get: Kim = (combined_height + 4) / 4

    kim_height = (combined_height + 4) / 4
    tamara_height = 3 * kim_height - 4
    result = tamara_height
    return result

print(solution())