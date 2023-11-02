def solution():
    # Convert the original length to inches
    length_in_inches = 4

    # Double the length twice
    length_in_inches *= 2
    length_in_inches *= 2

    # Convert the length back to the appropriate units
    current_length = f"{length_in_inches} inches"
    result = current_length
    return result

print(solution())