def solution():
    # define the cost of a smartphone
    smartphone_cost = 300

    # define the cost of a personal computer
    pc_cost = smartphone_cost + 500

    # define the cost of an advanced tablet
    tablet_cost = smartphone_cost + pc_cost

    # calculate the total cost of buying one of each product
    total_cost = smartphone_cost + pc_cost + tablet_cost

    result = total_cost
    return result

print(solution())