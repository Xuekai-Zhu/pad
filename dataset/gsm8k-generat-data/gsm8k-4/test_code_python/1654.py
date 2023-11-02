def solution():
    """Bob is building a garden on his land, and he wants it to be fenced in to keep out varmints. The garden is a rectangular plot 225 feet long by 125 feet wide. He also wants to have a small 3-foot wide gate to walk through and a larger 10-foot wide gate to move his gardening equipment through. How much fencing is Bob going to need to fence in his garden, taking into account the two gates?"""
    # Define the dimensions of the garden
    length = 225
    width = 125
    
    # Define the widths of the gates
    small_gate_width = 3
    large_gate_width = 10
    
    # Calculate the perimeter of the garden
    garden_perimeter = 2 * (length + width)
    
    # Calculate the length of fencing needed for the small gate
    small_gate_fence = small_gate_width
    
    # Calculate the length of fencing needed for the large gate
    large_gate_fence = large_gate_width
    
    # Calculate the total length of fencing needed, taking into account the gates
    total_fence = garden_perimeter + small_gate_fence + large_gate_fence
    
    # return the result
    result = total_fence
    return result

print(solution())