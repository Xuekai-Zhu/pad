def solution():
    # Calculate the number of passes thrown to the left of the field
    left_passes = (50 - 2) / 4  # the quarterback throws 2 more passes to the center than to the left, and throws twice as many passes to the right than to the left
    result = left_passes
    return result

print(solution())