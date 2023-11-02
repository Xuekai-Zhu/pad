def solution():
    # Calculate the height of the tree at the end of 2019
    height_2018 = 100 + (100 * 0.1)  # height at the end of 2018 with 10% growth
    height_2019 = height_2018 + (height_2018 * 0.1)  # height at the end of 2019 with 10% growth
    growth = height_2019 - 100  # total growth from 2017 to 2019
    result = growth
    return result

print(solution())