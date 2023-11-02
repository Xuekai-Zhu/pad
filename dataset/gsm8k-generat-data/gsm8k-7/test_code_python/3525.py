def solution():
    num_tattoos_jason = (2 * 2) + (3 * 2)  # Jason has 2 tattoos on each arm and 3 tattoos on each leg
    num_tattoos_adam = (2 * num_tattoos_jason) + 3  # Adam has three more than twice as many tattoos as Jason has
    result = num_tattoos_adam
    return result

print(solution())