def solution():
    # Calculate the total number of pizza slices left
    total_slices_left = 8 + 14 - (2*9)  # small pizza has 8 slices, large pizza has 14 slices, both have eaten 9 slices
    pieces_per_person = total_slices_left / 2  # divide by two as there are two people
    result = pieces_per_person
    return result

print(solution())