def solution():
    
    # Define the total number of quarts of tea left
    total_quarts = 10

    # Calculate the number of quarts drank by the students who drank 1.5 quarts of tea
    students_1_5 = 4 * 1.5

    # Calculate the number of quarts drank by the students who drank 2 quarts of tea
    students_2_5 = 16 * 2

    # Calculate the total number of quarts drank by the students who drank 1.5 quarts of tea
    total_quarts_1_5 = students_1_5 + students_2_5

    # Calculate the total number of gallons of tea at the beginning of the party
    gallons_start = total_quarts / 1000

    # Display the total number of gallons of tea at the beginning of the party
    result = gallons_start
    return result

print(solution())