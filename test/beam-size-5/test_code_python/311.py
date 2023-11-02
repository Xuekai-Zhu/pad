def solution():
    # Calculate the total number of people invited
    total_people = 2 * 6 + 3 * 4

    # Subtract the number of people who couldn't come due to illness
    total_people -= 8

    # Calculate the number of people who had previous commitments
    previous_commitments = total_people / 4

    # Calculate the total number of people who show up for Martha's party
    total_people = total_people + previous_commitments
    result = total_people
    return result

print(solution())