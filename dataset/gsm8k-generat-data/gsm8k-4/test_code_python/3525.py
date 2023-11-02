def solution():
    """Adam has three more than twice as many tattoos as Jason has. If Jason has two tattoos on each of his arms and three tattoos on each of his legs, how many tattoos does Adam have?"""
    # Calculate the number of tattoos Jason has on his arms and legs
    jason_arm_tattoos = 2 * 2
    jason_leg_tattoos = 3 * 2

    # Calculate the total number of tattoos Jason has
    jason_total_tattoos = jason_arm_tattoos + jason_leg_tattoos

    # Calculate the number of tattoos Adam has
    adam_tattoos = 3 + 2 * jason_total_tattoos

    # return the result
    result = adam_tattoos
    return result

print(solution())