def solution():
    
    # Define the ratio of electric poles to electric wires
    poles_to_wires_ratio = 1/3

    # Calculate the total number of electric wires needed
    total_wires = 45

    # Calculate the total number of electric poles needed
    total_poles = total_wires / (1 + poles_to_wires_ratio)

    # Display the total number of electric poles needed
    result = total_poles
    return result

print(solution())