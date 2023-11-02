def solution():
    """Martha has 18 crayons. She lost half of them, so she bought a new set of 20 crayons. How many crayons in total does Martha have after the purchase?"""
    # Define the initial number of crayons and the number she lost
    initial_crayons = 18
    lost_crayons = initial_crayons / 2

    # Calculate the total number of crayons after the purchase
    total_crayons = initial_crayons - lost_crayons + 20

    # Return the result
    result = total_crayons
    return result

print(solution())