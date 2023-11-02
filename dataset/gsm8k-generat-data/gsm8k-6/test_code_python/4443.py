def solution():
    # Calculate the total number of horses on the carousel
    blue_horses = 3
    purple_horses = 3 * 3  # three times the number of blue horses
    green_horses = 2 * purple_horses # twice the number of purple horses
    gold_horses = green_horses / 6  # 1/6th the number of green horses
    total_horses = blue_horses + purple_horses + green_horses + gold_horses
    result = total_horses
    return result

print(solution())