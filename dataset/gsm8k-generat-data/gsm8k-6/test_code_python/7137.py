def solution():
    # Calculate the total weight of all the macaroons
    total_weight = 12 * 5  # 12 macaroons weighing 5 ounces each

    # Calculate the weight of each bag before Steve ate one
    bag_weight = total_weight / 4 

    # Calculate the total weight remaining after Steve ate one bag
    remaining_weight = (bag_weight * 3)

    result = remaining_weight
    return result

print(solution())