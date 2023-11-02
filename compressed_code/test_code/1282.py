def solution():
    
    length = 225
    width = 125
    small_gate_width = 3
    large_gate_width = 10
    perimeter = 2 * (length + width)
    fence_length = perimeter - small_gate_width - large_gate_width
    result = fence_length
    return result

print(solution())