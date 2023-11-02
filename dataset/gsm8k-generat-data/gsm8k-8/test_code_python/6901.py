def solution():
    # Define the total number of slices
    total_slices = 12

    # Define how many slices each person ate
    per_person_slices = 4

    # Calculate how many friends were there with Ron
    friends = (total_slices - per_person_slices) / per_person_slices

    result = friends
    return result

print(solution())