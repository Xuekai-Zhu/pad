def solution():
    length = 225
    width = 125
    small_gate_width = 3
    large_gate_width = 10

    # Calculate the perimeter of the garden without the gates
    garden_perimeter = 2 * length + 2 * width

    # Calculate the length of fencing needed for the small gate
    small_gate_length = small_gate_width

    # Calculate the length of fencing needed for the large gate
    large_gate_length = large_gate_width

    # Calculate the total length of fencing needed
    total_fence_length = garden_perimeter + small_gate_length + large_gate_length
    result = total_fence_length
    return result

print(solution())