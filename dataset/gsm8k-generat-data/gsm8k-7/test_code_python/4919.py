def solution():
    eggs_saly = 10
    eggs_ben = 14
    eggs_ked = eggs_ben / 2
    num_weeks = 4

    # Calculate the total number of eggs needed in a month by all three people
    total_eggs = (eggs_saly + eggs_ben + eggs_ked) * num_weeks
    result = total_eggs
    return result

print(solution())