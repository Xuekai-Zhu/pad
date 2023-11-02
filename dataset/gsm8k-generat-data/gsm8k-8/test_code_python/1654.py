def solution():
    # Define the dimensions of the garden and the widths of the gates
    length = 225
    width = 125
    small_gate_width = 3
    large_gate_width = 10

    # Calculate the perimeter of the garden
    garden_perimeter = 2 * (length + width)

    # Calculate the length of fencing needed for the small gate
    small_gate_fencing = small_gate_width

    # Calculate the length of fencing needed for the large gate
    large_gate_fencing = large_gate_width

    # Calculate the total length of fencing needed, including both gates
    total_fencing = garden_perimeter + small_gate_fencing + large_gate_fencing
    result = total_fencing
    return result

print(solution())