def solution():
    num_boxes = 4
    donuts_per_box = 12

    # Calculate the total number of donuts
    total_donuts = num_boxes * donuts_per_box

    # Subtract the donuts given to Sophie's mom (1 box = 12 donuts)
    total_donuts -= 12

    # Subtract the donuts given to Sophie's sister (1/2 dozen = 6 donuts)
    total_donuts -= 6

    result = total_donuts
    return result

print(solution())