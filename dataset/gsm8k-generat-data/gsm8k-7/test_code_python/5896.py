def solution():
    num_girls = 6
    num_boys = 8

    # Calculate the total number of kids in the play
    total_kids = num_girls + num_boys

    # Calculate the total number of parents in the auditorium
    total_parents = total_kids * 2
    result = total_parents
    return result

print(solution())