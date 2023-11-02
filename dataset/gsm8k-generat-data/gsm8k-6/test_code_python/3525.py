def solution():
    # Calculate the number of tattoos Jason has
    tattoos_Jason = 2*2 + 3*2  # two tattoos on each of his legs and arms
    # Calculate the number of tattoos Adam has
    tattoos_Adam = 3 + 2*tattoos_Jason  # three more than twice as many tattoos as Jason has
    result = tattoos_Adam
    return result

print(solution())