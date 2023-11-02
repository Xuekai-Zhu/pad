def solution():
    # Calculate the number of people remaining in the first row
    first_row_remaining = 24 - 3

    # Calculate the number of people remaining in the second row
    second_row_remaining = 20 - 5

    # Calculate the total number of people remaining on the beach
    remaining_people = first_row_remaining + second_row_remaining + 18
    result = remaining_people
    return result

print(solution())