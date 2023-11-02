def solution():
    """A frog pond has five frogs living in it. Some frogs laid eggs, and now there are three times as many tadpoles growing into more frogs as there are frogs. Two-thirds of the tadpoles will survive to maturity as frogs. The pond can only sustain eight frogs. How many frogs will have to find a new pond when the tadpoles grow up?"""
    # Define the number of initial frogs living in the pond
    initial_frogs = 5

    # Calculate the number of tadpoles
    tadpoles = initial_frogs * 3

    # Calculate the number of frogs that will survive to maturity
    mature_frogs = tadpoles * 2/3

    # Calculate the total number of frogs in the pond
    total_frogs = initial_frogs + mature_frogs

    # Calculate the number of frogs that will have to find a new pond
    excess_frogs = max(0, total_frogs - 8)

    # Display the number of frogs that will have to find a new pond
    result = excess_frogs
    return result

print(solution())