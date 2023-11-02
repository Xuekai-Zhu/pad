def solution():
    # Define the number of cans needed for a normal batch of chili
    chilis = 1
    beans = 2
    tomatoes = 2 * 1.5  # 50% more than beans

    # Calculate the total cans needed for a quadruple batch of chili
    total_chilis = chilis * 4
    total_beans = beans * 4
    total_tomatoes = tomatoes * 4

    # Calculate the total number of cans of food needed
    total_cans = total_chilis + total_beans + total_tomatoes
    result = total_cans
    return result

print(solution())