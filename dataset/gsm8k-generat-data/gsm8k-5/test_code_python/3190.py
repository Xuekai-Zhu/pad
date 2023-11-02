def solution():
    num_boxes_to_trim = 30  # Neil needs to trim 30 boxwoods
    trim_cost = 5.00  # Neil charges $5.00 to trim each boxwood
    fancy_shape_cost = 15.00  # Neil charges $15.00 to shape each boxwood
    num_boxes_to_shape = 4  # Neil needs to shape 4 boxwoods

    # Calculate the total cost of trimming all 30 boxwoods
    total_trim_cost = num_boxes_to_trim * trim_cost

    # Calculate the total cost of shaping the 4 boxwoods
    total_shape_cost = num_boxes_to_shape * fancy_shape_cost

    # Calculate the total cost for all services performed
    total_cost = total_trim_cost + total_shape_cost
    result = total_cost
    return result

print(solution())