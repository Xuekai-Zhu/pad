def solution():
    # Calculate the number of firecrackers left after confiscation
    left_after_confiscation = 48 - 12

    # Calculate the number of good firecrackers
    good_firecrackers = left_after_confiscation - left_after_confiscation/6

    # Calculate the number of firecrackers set off
    set_off = good_firecrackers / 2

    result = set_off
    return result

print(solution())