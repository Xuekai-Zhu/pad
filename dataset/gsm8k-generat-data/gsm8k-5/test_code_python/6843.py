def solution():
    boxes_of_donuts = 4  # Sophie bought 4 boxes of donuts
    donuts_per_box = 12  # There are 12 donuts in each box
    total_donuts = boxes_of_donuts * donuts_per_box  # Calculate total number of donuts

    # Calculate number of donuts given to mom and sister
    donuts_given = (1 * donuts_per_box) + (0.5 * 12)

    # Calculate the number of donuts left for Sophie
    donuts_left = total_donuts - donuts_given
    result = donuts_left
    return result

print(solution())