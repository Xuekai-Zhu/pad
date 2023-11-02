def solution():
    mike_toys = 6  # Mike has 6 toys
    annie_toys = mike_toys * 3  # Annie has three times more toys than Mike
    tom_toys = annie_toys + 2  # Tom has two more toys than Annie

    # Calculate the total number of toys
    total_toys = mike_toys + annie_toys + tom_toys
    result = total_toys
    return result

print(solution())