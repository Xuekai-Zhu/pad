def solution():
    """Billy's family likes to keep their bicycles stored in the garage when they're not being used. They own a total of 4 bicycles. Each bicycle wheel has 10 spokes. How many spokes are inside the garage?"""
    num_bicycles = 4
    spokes_per_wheel = 10
    num_wheels = num_bicycles * 2
    num_spokes = num_wheels * spokes_per_wheel
    result = num_spokes
    return result

print(solution())