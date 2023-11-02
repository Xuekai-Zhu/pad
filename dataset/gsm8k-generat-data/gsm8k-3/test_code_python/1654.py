def solution():
    """Bob is building a garden on his land, and he wants it to be fenced in to keep out varmints. The garden is a rectangular plot 225 feet long by 125 feet wide. He also wants to have a small 3-foot wide gate to walk through and a larger 10-foot wide gate to move his gardening equipment through. How much fencing is Bob going to need to fence in his garden, taking into account the two gates?"""
    # Define the dimensions of the garden plot
    length = 225
    width = 125

    # Define the widths of the two gates
    small_gate_width = 3
    large_gate_width = 10

    # Calculate the length of fencing needed for the perimeter of the plot
    perimeter = 2 * (length + width)

    # Subtract the length of fencing needed for the small gate
    perimeter -= small_gate_width * 2

    # Subtract the length of fencing needed for the large gate
    perimeter -= large_gate_width

    # Display the total length of fencing needed
    result = perimeter
    return result

print(solution())