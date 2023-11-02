def solution():
    bonnie_apples = 8
    samuel_apples = bonnie_apples + 20

    # Calculate how many apples Samuel has left after eating half
    samuel_apples_left = samuel_apples / 2

    # Calculate how many apples Samuel used to make apple pie
    pie_apples = samuel_apples / 7

    # Calculate how many apples Samuel has left after making apple pie
    samuel_apples_left -= pie_apples

    result = samuel_apples_left
    return result

print(solution())