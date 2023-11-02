def solution():
    # Calculate the number of slices of pizza left
    slices_left = 16 - (16/4) - ((16/4)*(3/4)) - 4  # one-fourth was eaten during dinner, then one-fourth of the remaining was eaten by Yves, and his siblings ate 4 slices in total
    result = slices_left
    return result

print(solution())