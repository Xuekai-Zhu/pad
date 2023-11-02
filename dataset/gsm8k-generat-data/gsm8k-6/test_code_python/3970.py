def solution():
    # Calculate the amount of tomatoes, beans, and chilis needed for one normal batch of chili
    tomatoes = 2 * 1.5  # 50% more tomatoes than beans
    beans = 2
    chilis = 1

    # Calculate the total cans of food needed for a quadruple batch of chili
    total_tomatoes = tomatoes * 4
    total_beans = beans * 4
    total_chilis = chilis * 4
    total_cans = total_tomatoes + total_beans + total_chilis
    result = total_cans
    return result

print(solution())