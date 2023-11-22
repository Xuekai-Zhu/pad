def solution():
    
    # Define the number of children and the number of diapers per child
    NUM_CHILDREN = 2
    DIAPERS_PER_CHILD = 5

    # Calculate the total number of diapers
    total_diapers = NUM_CHILDREN * DIAPERS_PER_CHILD

    # Calculate the number of diapers Jordan's wife changes
    wife_changes = total_diapers / 2

    # Calculate the number of diapers Jordan changes per day
    jordan_changes = total_diapers - wife_changes

    # Display the number of diapers Jordan changes per day
    result = jordan_changes
    return result

print(solution())