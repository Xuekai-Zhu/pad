def solution():
    """Ali, Peter, and Joey were fishing. The fish Ali caught weighed, in sum, twice as much as the fish that Peter caught. Joey caught 1 kg more fish than Peter. Together the three of them caught 25 kg of fish. How many kilograms did Ali catch?"""
    # Let's assume Peter caught 'x' kg of fish
    x = 0

    # Calculate the weight of fish caught by Joey
    y = x + 1

    # Calculate the weight of fish caught by Ali
    z = 2 * (x + y)

    # Calculate the total weight of fish caught by all of them
    total_weight = x + y + z

    # Check if the total weight is equal to 25 kg
    if total_weight == 25:
        result = z
    else:
        result = "No valid solution exists."

    return result

print(solution())