def solution():
    """Bob is building a garden on his land, and he wants it to be fenced in to keep out varmints. The garden is a rectangular plot 225 feet long by 125 feet wide. He also wants to have a small 3-foot wide gate to walk through and a larger 10-foot wide gate to move his gardening equipment through. How much fencing is Bob going to need to fence in his garden, taking into account the two gates?"""
    length = 225
    width = 125
    small_gate_width = 3
    large_gate_width = 10
    perimeter = 2 * (length + width)
    fence_length = perimeter - small_gate_width - large_gate_width
    result = fence_length
    return result

print(solution())