def solution():
    """Ali, Peter, and Joey were fishing. The fish Ali caught weighed, in sum, twice as much as the fish that Peter caught. Joey caught 1 kg more fish than Peter. Together the three of them caught 25 kg of fish. How many kilograms did Ali catch?"""
    total_weight = 25
    peters_weight = x
    joeys_weight = x + 1
    alis_weight = 2 * peters_weight

    # Set up equation to solve for x
    equation = peters_weight + joeys_weight + alis_weight - total_weight

    # Solve for x
    x = equation / 4

    # Calculate Ali's weight
    alis_weight = 2 * x

    return alis_weight

print(solution())