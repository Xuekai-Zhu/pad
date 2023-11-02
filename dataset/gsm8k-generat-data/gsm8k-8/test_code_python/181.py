def solution():
    # Define the initial height and growth rate
    height = 100
    growth_rate = 1.1

    # Calculate the height of the tree at the end of 2018 and 2019
    height_2018 = height * growth_rate
    height_2019 = height_2018 * growth_rate

    # Calculate the total growth of the tree
    total_growth = height_2019 - height

    result = total_growth
    return result

print(solution())