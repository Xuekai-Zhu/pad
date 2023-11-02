def solution():
    largest_doll = 243
    size_ratio = 2 / 3

    # Calculate the size of the 2nd biggest doll
    second_doll = largest_doll * size_ratio

    # Calculate the size of the 3rd biggest doll
    third_doll = second_doll * size_ratio

    # Continue calculating the size of each doll until the 6th biggest
    fourth_doll = third_doll * size_ratio
    fifth_doll = fourth_doll * size_ratio
    sixth_doll = fifth_doll * size_ratio

    result = sixth_doll
    return result

print(solution())