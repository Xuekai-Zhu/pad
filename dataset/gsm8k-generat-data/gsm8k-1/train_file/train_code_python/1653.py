def solution():
    """Bob is building a garden on his land, and he wants it to be fenced in to keep out varmints. The garden is a rectangular plot 225 feet long by 125 feet wide. He also wants to have a small 3-foot wide gate to walk through and a larger 10-foot wide gate to move his gardening equipment through. How much fencing is Bob going to need to fence in his garden, taking into account the two gates?"""
    length = 225
    width = 125
    gate1_width = 3
    gate2_width = 10
    perimeter = (2 * length) + (2 * width)
    perimeter_with_gates = perimeter + gate1_width + gate2_width
    result = perimeter_with_gates
    return result

print(solution())