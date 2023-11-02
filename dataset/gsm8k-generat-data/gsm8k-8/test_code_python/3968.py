def solution():
    # Let's assume there are x brown eggs in total
    x = 5  # Since we know that 5 brown eggs were left after the accident

    # We also know that Linda had 3 times as many white eggs as brown eggs
    white_eggs = 3 * x

    # Linda had a total of x + white_eggs eggs before the accident
    total_eggs_before = x + white_eggs

    # After the accident, Linda had a dozen eggs left, which is 12 in total
    total_eggs_after = 12

    # Therefore, Linda must have broken total_eggs_before - total_eggs_after eggs
    eggs_broken = total_eggs_before - total_eggs_after

    result = eggs_broken
    return result

print(solution())