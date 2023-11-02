def solution():
    # Calculate the number of eggs collected every week
    eggs_collected_per_week = (270 + 3) * 7  # 270 hens and 3 roosters live in the chicken coop, and eggs are collected every day of the week

    # Calculate the number of boxes of eggs
    boxes_of_eggs = eggs_collected_per_week // 6  # eggs are put in boxes of 6

    result = boxes_of_eggs
    return result

print(solution())