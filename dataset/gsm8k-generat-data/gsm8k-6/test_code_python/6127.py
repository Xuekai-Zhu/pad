def solution():
    # Calculate the thickness of the blanket after 4 foldings
    thickness = 3 * (2**4)  # the thickness doubles every time it is folded, and it starts out at 3 inches
    result = thickness
    return result

print(solution())