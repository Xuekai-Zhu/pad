def solution():
    """Samuel is arranging his grandma’s teacups. They are stored in boxes and inside the boxes, they are stacked 5 rows high with 4 cups in each row. Of the 26 boxes in her attic, 6 of the boxes contain pans, half of the remaining boxes contain decorations, and the rest of the boxes contain her teacups. Samuel breaks 2 of the cups every time he picks up one of the boxes. By the time Samuel has taken all of the teacups out of the boxes, how many teacups are left?"""
    # Define the number of rows and cups in each box
    ROWS_PER_BOX = 5
    CUPS_PER_ROW = 4

    # Calculate the total number of teacups in all the boxes
    total_cups = (26 - 6) / 2 * ROWS_PER_BOX * CUPS_PER_ROW

    # Calculate the number of teacups that Samuel breaks
    cups_broken = 2 * (26 - 6 - (26 - 6) / 2)

    # Calculate the number of teacups left
    teacups_left = total_cups - cups_broken

    # Display the number of teacups left
    result = teacups_left
    return result

print(solution())