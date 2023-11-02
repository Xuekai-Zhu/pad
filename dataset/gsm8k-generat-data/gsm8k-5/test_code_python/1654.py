def solution():
    length = 225  # Length of the rectangular plot
    width = 125  # Width of the rectangular plot
    small_gate_width = 3  # Width of the small gate
    large_gate_width = 10  # Width of the large gate

    # Calculate the perimeter of the rectangular plot
    perimeter = 2 * (length + width)

    # Subtract the width of the small gate from the perimeter
    perimeter -= small_gate_width

    # Subtract the width of the large gate from the perimeter
    perimeter -= large_gate_width

    result = perimeter
    return result

print(solution())