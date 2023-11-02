def solution():
    emily_marbles = 6

    # Megan gives Emily double her own number of marbles
    megan_marbles = emily_marbles * 2
    emily_marbles += megan_marbles

    # Emily gives Megan back half of her new total plus 1
    emily_marbles -= ((emily_marbles / 2) + 1)

    result = emily_marbles
    return result

print(solution())