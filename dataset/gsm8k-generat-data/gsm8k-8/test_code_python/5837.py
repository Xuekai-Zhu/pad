def solution():
    # Define the amount each roll can wrap
    shirt_boxes_per_roll = 5
    xl_boxes_per_roll = 3

    # Calculate the number of rolls needed for each type of box
    shirt_rolls_needed = ((20-1) // shirt_boxes_per_roll) + 1
    xl_rolls_needed = ((12-1) // xl_boxes_per_roll) + 1

    # Calculate the total rolls needed
    total_rolls_needed = shirt_rolls_needed + xl_rolls_needed

    # Calculate the total cost
    total_cost = total_rolls_needed * 4.00
    result = total_cost
    return result

print(solution())