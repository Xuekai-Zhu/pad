def solution():
    # Calculate the perimeter of the garden
    perimeter = 2 * (225 + 125)

    # Calculate the length of the fencing needed for the small gate
    small_gate_length = 3

    # Calculate the length of the fencing needed for the large gate
    large_gate_length = 10

    # Add the length of the fencing needed for the gates to the perimeter
    total_length = perimeter + small_gate_length + large_gate_length

    result = total_length
    return result

print(solution())