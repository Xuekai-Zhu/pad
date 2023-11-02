def solution():
    jeremy_bags = 3
    stacy_bags = 4
    total_bags = 10

    # Calculate the remaining number of bags needed after Jeremy and Stacy buy their chips
    remaining_bags = total_bags - jeremy_bags - stacy_bags

    # Calculate the number of bags of chips that Emily should buy
    emily_bags = remaining_bags
    result = emily_bags
    return result

print(solution())