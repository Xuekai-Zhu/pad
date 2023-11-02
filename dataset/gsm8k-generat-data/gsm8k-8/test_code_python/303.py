def solution():
    # Calculate the total amount of flour needed
    total_flour_needed = 12 * 4

    # Calculate how many bags of each size are needed to get enough flour
    bags_10_lb = total_flour_needed // 10
    bags_12_lb = total_flour_needed // 12
    if total_flour_needed % 10 != 0:
        bags_10_lb += 1
    if total_flour_needed % 12 != 0:
        bags_12_lb += 1

    # Calculate the cost of each type of bag
    cost_10_lb = bags_10_lb * 10
    cost_12_lb = bags_12_lb * 13

    # Choose the cheaper option and calculate the total cost
    if cost_10_lb <= cost_12_lb:
        total_cost = cost_10_lb
    else:
        total_cost = cost_12_lb

    result = total_cost
    return result

print(solution())