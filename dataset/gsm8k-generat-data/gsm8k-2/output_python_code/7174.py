def solution():
    """A frog pond has five frogs living in it. Some frogs laid eggs, and now there are three times as many tadpoles growing into more frogs as there are frogs. Two-thirds of the tadpoles will survive to maturity as frogs. The pond can only sustain eight frogs. How many frogs will have to find a new pond when the tadpoles grow up?"""
    initial_frogs = 5
    tadpoles = 3 * initial_frogs
    mature_frogs = round(tadpoles * (2 / 3))
    total_frogs = initial_frogs + mature_frogs
    surplus_frogs = total_frogs - 8
    result = surplus_frogs if surplus_frogs > 0 else 0
    return result

print(solution())