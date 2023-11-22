def solution():
    
    # Define the number of boxes per full pencil
    JAM_BOXES_PER_FULL_PENCIL = 3

    # Define the number of pencils Jam has
    JAM_HARDS_PER_FULL_PENCIL = 26

    # Define the number of pencils Meg has
    Meg_HARDS_PER_FULL_PENCIL = 46

    # Calculate the total number of pencils Jam and Meg have
    total_pencils = JAM_HARDS_PER_FULL_PENCIL + (2 * Meg_HARDS_PER_FULL_PENCIL)

    # Calculate the total number of boxes Jam and Meg need to store all their pencils
    total_boxes = total_pencils // (JAM_BOXES_PER_FULL_PENCIL + 2 * JAM_HARDS_PER_FULL_PENCIL)

    # Display the total number of boxes
    result = total_boxes
    return result

print(solution())