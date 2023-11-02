def solution():
    # Define the function of a parachute and the presence of atmosphere
    parachute_function = "create drag"
    atmosphere_present = True
    # Check if a parachute can function in a vacuum
    if parachute_function and not atmosphere_present:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())