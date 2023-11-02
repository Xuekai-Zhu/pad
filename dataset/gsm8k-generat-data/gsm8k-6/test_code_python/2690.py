def solution():
    # Calculate the total number of apples that Samuel bought
    apples_Samuel = 8 + 20  # Samuel bought 20 more apples than Bonnie

    # Calculate the number of apples Samuel had left after eating half of them
    apples_left = apples_Samuel / 2  # Samuel ate half of the apples

    # Calculate the number of apples Samuel had left after using 1/7 of them to make apple pie
    apples_left -= apples_Samuel / 7  # Samuel used 1/7 of the apples to make pie

    result = apples_left
    return result

print(solution())