def solution():
    # Megan gives Emily double the number of marbles she has
    emily_marbels = 6 + (2 * 2)  # Emily now has 10 marbles
    # Emily gives Megan back half of her new total plus 1
    emily_marbels -= ((emily_marbels / 2) + 1)
    result = emily_marbels
    return result

print(solution())