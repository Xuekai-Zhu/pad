def solution():
    # Calculate the number of slices needed for one family member
    slices_per_person = 20

    # Calculate the total number of slices needed for the family
    total_slices = slices_per_person * 8

    # Calculate the number of tomatoes needed
    tomatoes_needed = total_slices / 8

    result = tomatoes_needed
    return result

print(solution())