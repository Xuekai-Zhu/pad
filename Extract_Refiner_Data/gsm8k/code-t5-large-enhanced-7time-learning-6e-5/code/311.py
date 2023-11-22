def solution():
    
    # Define the number of people in each family
    family1 = 6
    family2 = 6
    family3 = 4

    # Calculate the total number of people
    total_people = family1 + family2 + family3

    # Subtract the number of people who couldn't come due to illness
    total_people -= 8

    # Calculate the number of people who had previous commitments
    previous_commitments = total_people / 4

    # Calculate the total number of people who showed up
    total_people += previous_commitments

    # Display the total number of people
    result = total_people
    return result

print(solution())