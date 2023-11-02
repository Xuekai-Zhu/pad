def solution():
    total_slices = 12
    slices_per_person = 4

    # Calculate the number of friends by dividing the total slices by the slices per person
    num_friends = total_slices / slices_per_person - 1 # subtract 1 to exclude Ron
    result = num_friends
    return result

print(solution())