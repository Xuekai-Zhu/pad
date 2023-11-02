def solution():
    """Adam has three more than twice as many tattoos as Jason has.  If Jason has two tattoos on each of his arms and three tattoos on each of his legs, how many tattoos does Adam have?"""
    # Calculate the number of tattoos Jason has
    jason_arm_tattoos = 2 * 2
    jason_leg_tattoos = 2 * 3
    jason_total_tattoos = jason_arm_tattoos + jason_leg_tattoos

    # Calculate the number of tattoos Adam has
    adam_tattoos = 2 * jason_total_tattoos + 3

    # Display the number of tattoos Adam has
    result = adam_tattoos
    return result

print(solution())