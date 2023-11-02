def solution():
    # Calculate the total weight of all macaroons
    total_weight = 12 * 5

    # Calculate the weight of one brown bag
    bag_weight = total_weight / 4

    # Calculate the weight of the macaroons in each bag
    macaroon_weight = bag_weight / (12/4)

    # Calculate the weight of the macaroons remaining after Steve ate one bag
    remaining_weight = (3 * bag_weight) - macaroon_weight

    result = remaining_weight
    return result

print(solution())