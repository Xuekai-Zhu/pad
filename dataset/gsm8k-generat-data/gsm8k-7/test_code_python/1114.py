def solution():
    num_donuts = 10
    num_days = 12
    num_donuts_eaten_by_jeff_per_day = 1
    num_donuts_eaten_by_chris = 8
    donuts_per_box = 10

    # Calculate the total number of donuts Jeff made
    total_donuts = num_donuts * num_days

    # Calculate the total number of donuts eaten by Jeff and Chris
    total_donuts_eaten = (num_donuts_eaten_by_jeff_per_day * num_days) + num_donuts_eaten_by_chris

    # Calculate the total number of donuts left
    total_donuts_left = total_donuts - total_donuts_eaten

    # Calculate the number of boxes that can be filled with the remaining donuts
    num_boxes = total_donuts_left // donuts_per_box
    result = num_boxes
    return result

print(solution())