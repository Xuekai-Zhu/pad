def solution():
    """Ali, Peter, and Joey were fishing. The fish Ali caught weighed, in sum, twice as much as the fish that Peter caught. Joey caught 1 kg more fish than Peter. Together the three of them caught 25 kg of fish. How many kilograms did Ali catch?"""
    # Let x be the weight of the fish that Peter caught
    x = 0

    # Calculate the weight of the fish that Joey caught
    y = x + 1

    # Calculate the weight of the fish that Ali caught
    z = 2 * (x + y)

    # Calculate the total weight of the fish
    total_weight = x + y + z

    # Set up an equation to solve for x
    # x + x + 1 + 2*(x+x+1) = 25
    # simplify to
    # 5x + 5 = 25
    # solve for x
    x = 4

    # Calculate the weight of the fish that Joey caught
    y = x + 1

    # Calculate the weight of the fish that Ali caught
    z = 2 * (x + y)

    # Display the weight of the fish that Ali caught
    result = z
    return result

print(solution())