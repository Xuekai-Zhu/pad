def solution():
    # Calculate the number of bags of chips Jeremy buys
    jeremy_bags = 3

    # Calculate the number of bags of chips Stacy buys
    stacy_bags = 4

    # Calculate the number of bags of chips Emily needs to buy
    total_bags = 10
    emily_bags = total_bags - jeremy_bags - stacy_bags

    result = emily_bags
    return result

print(solution())