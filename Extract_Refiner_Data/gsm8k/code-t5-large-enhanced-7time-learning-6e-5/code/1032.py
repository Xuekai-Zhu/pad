def solution():
    
    # Define the number of apples in one box and the number of boxes ordered
    APPLES_PER_BOX = 40
    BOXES_ordered = 2

    # Calculate the total number of apples
    total_apples = APPLES_PER_BOX * BOXES_ordered

    # Calculate the number of packs of apples that can be made
    packs = total_apples // 8

    # Display the number of packs
    result = packs
    return result

print(solution())