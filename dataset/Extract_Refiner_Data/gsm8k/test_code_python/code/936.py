def solution():
    
    # Define the number of children standing in a row and the number of rows for each School
    CHOOLS_PER_ROW = 8
    ROWS_PER_SCHOOL = 7

    # Calculate the total number of children standing
    total_children_stand = CHOOLS_PER_ROW * ROWS_PER_SCHOOL * CHOOLS_PER_ROW

    # Display the total number of children
    result = total_children_stand
    return result

print(solution())