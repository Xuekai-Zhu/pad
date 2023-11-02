def solution():
    blue_horses = 3
    purple_horses = 3 * blue_horses
    green_horses = 2 * purple_horses
    gold_horses = 1/6 * green_horses

    total_horses = blue_horses + purple_horses + green_horses + gold_horses

    result = total_horses
    return result

print(solution())