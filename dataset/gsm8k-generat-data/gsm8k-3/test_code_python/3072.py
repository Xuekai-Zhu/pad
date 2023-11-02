def solution():
    """Martha has 18 crayons. She lost half of them, so she bought a new set of 20 crayons. How many crayons in total does Martha have after the purchase?"""
    # Calculate the number of crayons Martha lost
    lost_crayons = 18 / 2

    # Calculate the total number of crayons after the loss
    total_crayons = 18 - lost_crayons

    # Add the new set of crayons
    total_crayons += 20

    # Display the total number of crayons Martha has
    result = total_crayons
    return result

print(solution())