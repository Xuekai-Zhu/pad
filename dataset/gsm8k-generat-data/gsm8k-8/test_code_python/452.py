def solution():
    # Emily starts with 6 marbles
    emily_marbles = 6

    # Megan gives Emily double the number of marbles she has (12)
    emily_marbles += 12

    # Emily gives Megan back half of her new total (9) plus 1, leaving Emily with 9 marbles
    emily_marbles -= ((emily_marbles / 2) + 1)

    result = emily_marbles
    return result

print(solution())