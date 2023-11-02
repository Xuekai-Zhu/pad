def solution():
    path_length = 900
    pole_spacing = 6
    bridge_length = 42

    # Calculate the effective length of the path (subtracting the bridge length)
    effective_length = path_length - bridge_length

    # Calculate the number of pole placements needed on one side of the path
    num_poles = effective_length / pole_spacing

    # Double the number of pole placements to account for both sides of the path
    total_poles = num_poles * 2
    result = total_poles
    return result

print(solution())