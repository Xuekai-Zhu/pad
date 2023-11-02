def solution():
    length = 225
    width = 125
    small_gate_width = 3
    large_gate_width = 10
    fence_length = (2 * length) + (2 * width) - (2 * small_gate_width) - (2 * large_gate_width)
    result = fence_length
    return result

print(solution())