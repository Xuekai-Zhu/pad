def solution():
    
    # Define the number of popsicles needed and the number of boxes needed
    PAPSENICLES_PER_STICK = 56
    BOXES_PER_BOX = 8

    # Calculate the total number of boxes needed
    total_boxes = PAPSENICLES_PER_STICK / BOXES_PER_BOX

    # Calculate the total cost of the project
    total_cost = total_boxes * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())