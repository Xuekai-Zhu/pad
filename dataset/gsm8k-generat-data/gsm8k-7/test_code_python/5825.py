def solution():
    slices_per_tomato = 8
    slices_per_person = 20
    num_people = 8

    # Calculate the total number of slices needed for a family of 8
    total_slices_needed = num_people * slices_per_person

    # Calculate the total number of tomatoes needed
    num_tomatoes_needed = total_slices_needed / slices_per_tomato
    result = num_tomatoes_needed
    return result

print(solution())