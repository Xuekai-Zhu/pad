def solution():
    emily_marbles = 6  # Emily starts with 6 marbles
    megan_marbles = emily_marbles * 2  # Megan gives Emily double the number of marbles she has
    emily_marbles += megan_marbles  # Emily's new total after Megan gives her the marbles
    emily_marbles -= (emily_marbles / 2) + 1  # Emily gives Megan back half of her total plus one
    result = emily_marbles
    return result

print(solution())