def solution():
    # Calculate the total distance driven
    total_distance = 15 + 6 + 2 + 4 + 11

    # Calculate the gallons of gas used
    gallons_used = total_distance / 19

    # Calculate the gallons of gas Kennedy started with
    starting_gas = gallons_used + 1
    result = starting_gas
    return result

print(solution())