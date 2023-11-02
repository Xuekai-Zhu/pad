def solution():
    """Adam has three more than twice as many tattoos as Jason has. If Jason has two tattoos on each of his arms and three tattoos on each of his legs, how many tattoos does Adam have?"""
    jason_tattoos_arms = 2 * 2 #2 tattoos on each of his arms
    jason_tattoos_legs = 3 * 2 #3 tattoos on each of his legs
    jason_total_tattoos = jason_tattoos_arms + jason_tattoos_legs
    adam_total_tattoos = 3 + 2*jason_total_tattoos
    result = adam_total_tattoos
    return result

print(solution())