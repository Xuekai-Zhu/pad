def solution():
    # Calculate the number of tadpoles
    frogs = 5
    tadpoles = 3 * frogs

    # Calculate the number of frogs that will survive to maturity
    mature_frogs = 2 * (tadpoles * 2/3)  # Two-thirds of tadpoles survive to maturity

    # Calculate the number of frogs that will have to find a new pond
    excess_frogs = mature_frogs - 8
    if excess_frogs < 0:
        excess_frogs = 0  # There are not enough frogs to exceed the pond's capacity

    result = excess_frogs
    return result

print(solution())