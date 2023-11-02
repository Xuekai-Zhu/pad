def solution():
    """Billy's family likes to keep their bicycles stored in the garage when they're not being used. They own a total of 4 bicycles. Each bicycle wheel has 10 spokes. How many spokes are inside the garage?"""
    bikes_owned = 4
    wheels_per_bike = 2
    spokes_per_wheel = 10
    total_spokes = bikes_owned * wheels_per_bike * spokes_per_wheel
    result = total_spokes
    return result

print(solution())