def solution():
    total_slices = 12  # The pizza had 12 slices in total
    slices_per_person = 4  # Each person ate 4 slices
    ron_slices = slices_per_person  # Ron is one of the people who ate 4 slices

    # Calculate the number of friends Ron had
    num_friends = (total_slices - ron_slices) / slices_per_person
    result = num_friends
    return result

print(solution())