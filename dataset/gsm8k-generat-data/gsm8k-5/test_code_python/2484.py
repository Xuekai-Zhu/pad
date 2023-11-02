def solution():
    # Calculate number of people in the first row after 3 leave
    first_row = 24 - 3

    # Calculate number of people in the second row after 5 leave
    second_row = 20 - 5

    # Calculate total number of people left on the beach
    total_people = first_row + second_row + 18
    result = total_people
    return result

print(solution())