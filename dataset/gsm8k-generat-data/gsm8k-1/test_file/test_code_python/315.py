def solution():
    """The ratio of the electric poles and electric wires needed to connect and supply the electricity in a certain neighborhood is 1:3. If the total number of electric wires needed to connect the electricity in the neighborhood is 45, calculate the total number of electric poles required by an electric company to supply the electricity in the neighborhood."""
    ratio = 1/3
    wires = 45
    poles = ratio * wires / (1 - ratio) # Use ratio formula to solve for poles
    result = poles
    return result

print(solution())