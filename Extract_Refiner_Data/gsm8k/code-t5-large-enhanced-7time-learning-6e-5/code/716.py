def solution():
    
    # Define the number of boxes of coco Crunch and Fruit Loops bought this week
    coco_crunch = 3
    fruit_loops = 5

    # Define the number of boxes of cereal bought last week
    cereal_last_week = 4

    # Calculate the total number of boxes of cereal bought this week
    total_cereal = coco_crunch + fruit_loops

    # Calculate the difference in the number of boxes of cereal bought this week and last week
    difference = total_cereal - cereal_last_week

    # Display the difference in the number of boxes of cereal bought this week
    result = difference
    return result

print(solution())