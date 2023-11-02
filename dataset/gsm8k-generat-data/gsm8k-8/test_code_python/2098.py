def solution():
    # Calculate the number of eggs laid each day
    eggs_laid_per_day = 270

    # Calculate the number of eggs collected each day
    eggs_collected_per_day = eggs_laid_per_day * 1.03

    # Calculate the number of eggs collected each week
    eggs_collected_per_week = eggs_collected_per_day * 7

    # Calculate the number of boxes of eggs
    boxes_of_eggs = eggs_collected_per_week / 6

    result = boxes_of_eggs
    return result

print(solution())