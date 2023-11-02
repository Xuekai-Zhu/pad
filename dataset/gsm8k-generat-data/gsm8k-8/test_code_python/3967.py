def solution():
    # Calculate the initial number of roses
    initial_roses = 2 * 12 + 1 * 12

    # Calculate the number of roses left after the chocolates were traded
    roses_left = initial_roses + 1 * 12

    # Calculate the number of roses left after the first round of wilting
    roses_after_first_wilting = roses_left / 2

    # Calculate the number of roses left after the second round of wilting
    roses_after_second_wilting = roses_after_first_wilting / 2

    # Calculate the number of unwilted roses
    unwilted_roses = roses_after_second_wilting

    result = unwilted_roses
    return result

print(solution())