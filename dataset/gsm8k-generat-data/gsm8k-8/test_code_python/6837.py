def solution():
    # Define the initial number of crayons
    initial_crayons = 21

    # Add the number of crayons in Annie's locker
    total_crayons = initial_crayons + 36

    # Calculate the amount that Bobby gave Annie
    bobby_crayons = 36 / 2

    # Add Bobby's crayons to Annie's total
    total_crayons += bobby_crayons

    # Calculate the amount of crayons Annie gives to Mary
    mary_crayons = total_crayons / 3
    result = mary_crayons
    return result

print(solution())