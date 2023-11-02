def solution():
    # Calculate the ratio of electric poles to electricity
    electric_poles_ratio = 1/3

    # Calculate the total number of electric wires needed
    electric_wires_needed = 45

    # Calculate the total number of electric poles needed
    electric_poles_needed = electric_wires_needed * electric_poles_ratio

    result = electric_poles_needed
    return result

print(solution())