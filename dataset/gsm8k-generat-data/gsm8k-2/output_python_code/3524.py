def solution():
    """Adam has three more than twice as many tattoos as Jason has. If Jason has two tattoos on each of his arms and three tattoos on each of his legs, how many tattoos does Adam have?"""
    jason_tattoos = (2*2) + (2*3)
    adam_tattoos = 2*jason_tattoos + 3
    result = adam_tattoos
    return result

print(solution())