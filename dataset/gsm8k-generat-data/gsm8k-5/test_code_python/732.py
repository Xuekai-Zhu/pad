def solution():
    # Calculate the number of eggs in 5 egg sacs
    eggs = 1000 * 5

    # Calculate the number of baby tarantula legs in 5 egg sacs
    legs_total = eggs * 8

    # Calculate the number of baby tarantula legs in one less than 5 egg sacs
    legs_less_one = (eggs - 1) * 8
    result = legs_less_one
    return result

print(solution())