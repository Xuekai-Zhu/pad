def solution():
    """A frog pond has five frogs living in it. Some frogs laid eggs, and now there are three times as many tadpoles growing into more frogs as there are frogs. Two-thirds of the tadpoles will survive to maturity as frogs. The pond can only sustain eight frogs. How many frogs will have to find a new pond when the tadpoles grow up?"""
    # Define the initial number of frogs
    initial_frogs = 5

    # Calculate the number of tadpoles
    tadpoles = initial_frogs * 3

    # Calculate the number of frogs that will survive to maturity
    mature_frogs = round(tadpoles * (2/3))

    # Calculate the total number of frogs in the pond after the tadpoles grow up
    total_frogs = initial_frogs + mature_frogs

    # Calculate the number of frogs that need to find a new pond
    if total_frogs > 8:
        new_pond_frogs = total_frogs - 8
    else:
        new_pond_frogs = 0

    # return the result
    result = new_pond_frogs
    return result

print(solution())