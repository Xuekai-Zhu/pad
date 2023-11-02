def solution():
    slices_left = 12  # start with 12 slices
    slices_left /= 2  # ate half of the pizza, so divide by 2
    slices_left *= (2/3)  # ate 1/3 of the remaining pizza, so multiply by 2/3
    result = slices_left
    return result

print(solution())