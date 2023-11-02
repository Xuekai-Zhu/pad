def solution():
    # Calculate the sum of dollars raised from each level of financial backing
    level_1 = 10 * 10 * 10 * 2  # highest level is ten times as high as the previous one, and there are two backers at this level
    level_2 = 10 * 10 * 3  # second level is ten times as high as the first level, and there are three backers at this level
    level_3 = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10  # lowest level is the base level, and there are ten backers at this level
    total_raised = level_1 + level_2 + level_3

    # Calculate the value of the highest level of financial backing
    highest_level = total_raised/12  # He needs to raise $12000 to get his business off the ground
    result = highest_level
    return result

print(solution())