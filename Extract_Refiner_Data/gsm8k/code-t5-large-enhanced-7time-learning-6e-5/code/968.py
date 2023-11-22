def solution():
    
    # Define the number of boxes and oranges per box
    BOXES = 12
    ORANGES_PER_BOX = 20

    # Calculate the total number of oranges given away
    given_oranges = 2 * ORANGES_PER_BOX

    # Calculate the total number of oranges sold
    sold_oranges = BOXES - given_oranges

    # Calculate the number of oranges Mrs. Harrington kept
    kept_oranges = sold_oranges / 4

    # Calculate the number of oranges Mrs. Harrington sold
    sold_oranges_sold = sold_oranges - kept_oranges

    # Display the number of oranges Mrs. Harrington sold
    result = sold_oranges_sold
    return result

print(solution())