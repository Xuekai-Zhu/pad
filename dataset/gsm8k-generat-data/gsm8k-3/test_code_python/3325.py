def solution():
    """Billy's family likes to keep their bicycles stored in the garage when they're not being used.  They own a total of 4 bicycles.  Each bicycle wheel has 10 spokes.  How many spokes are inside the garage?"""
    # Define the number of bicycles
    num_bicycles = 4

    # Define the number of spokes per bicycle wheel
    num_spokes_per_wheel = 10

    # Calculate the total number of spokes in the garage
    total_spokes = num_bicycles * 2 * num_spokes_per_wheel

    # Display the total number of spokes in the garage
    result = total_spokes
    return result

print(solution())