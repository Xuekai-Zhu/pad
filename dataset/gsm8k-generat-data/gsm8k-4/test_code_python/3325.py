def solution():
    """Billy's family likes to keep their bicycles stored in the garage when they're not being used. They own a total of 4 bicycles. Each bicycle wheel has 10 spokes. How many spokes are inside the garage?"""
    # Define the number of bicycles and spokes per wheel
    bicycles = 4
    spokes_per_wheel = 10

    # Calculate the total number of spokes in the garage
    total_spokes = bicycles * 2 * spokes_per_wheel

    # return the result
    result = total_spokes
    return result

print(solution())