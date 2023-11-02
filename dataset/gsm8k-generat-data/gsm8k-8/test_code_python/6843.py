def solution():
    # Define the number of boxes and donuts per box
    num_boxes = 4
    donuts_per_box = 12

    # Calculate the total number of donuts
    total_donuts = num_boxes * donuts_per_box

    # Subtract the donuts given away
    total_donuts -= donuts_per_box
    total_donuts -= 6

    # Calculate the number of donuts left for Sophie
    donuts_left = total_donuts
    result = donuts_left
    return result

print(solution())