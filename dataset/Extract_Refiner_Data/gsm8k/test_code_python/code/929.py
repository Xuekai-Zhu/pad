def solution():
    
    # Define the number of boxes donated by 10 people
    boxes_donated = 10 * 5

    # Define the number of boxes already in the group
    boxes_in_group = 10 * 10

    # Define the number of boxes needed per table
    boxes_per_table = 2

    # Define the number of tables the group already owns
    tables_owned = 15

    # Calculate the total number of boxes needed
    total_boxes = boxes_donated + boxes_in_group

    # Calculate the number of tables needed
    tables_needed = total_boxes / boxes_per_table

    # Display the number of tables needed
    result = tables_needed
    return result

print(solution())