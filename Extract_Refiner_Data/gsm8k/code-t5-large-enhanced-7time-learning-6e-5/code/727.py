def solution():
    
    # Define the number of smores per sleeve and the number of sleeves per box
    SMORES_PER_SLEE = 8
    SLEEPS_PER_BOX = 3

    # Calculate the total number of smores needed
    total_smores = 9 * 2 + 6 * 1

    # Calculate the total number of boxes needed
    total_boxes = total_smores / SMORES_PER_SLEE * SLEEPS_PER_BOX

    # Display the total number of boxes needed
    result = total_boxes
    return result

print(solution())