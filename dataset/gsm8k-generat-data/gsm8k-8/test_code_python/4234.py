def solution():
    # Calculate the number of cats in King Henry's kingdom
    hogs_to_cats_ratio = 3
    hogs_number = 75
    cats_number = hogs_number / hogs_to_cats_ratio

    # Calculate 60% of the number of cats and subtract 5
    cats_percent = 60
    cats_percent_decimal = cats_percent / 100
    cats_percent_number = cats_percent_decimal * cats_number
    result = cats_percent_number - 5
    return result

print(solution())