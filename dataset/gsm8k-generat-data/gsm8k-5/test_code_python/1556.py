def solution():
    slices_left = 4  # There are 4 slices of pizza left
    slices_per_person = 2  # Each person ate 2 slices of pizza

    # Calculate the total number of slices eaten by the group
    total_slices_eaten = 16 - slices_left
    # Divide the total slices by the slices per person to get the number of people
    num_people = total_slices_eaten / slices_per_person
    result = num_people
    return result

print(solution())