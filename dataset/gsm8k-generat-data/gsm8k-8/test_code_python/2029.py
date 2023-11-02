def solution():
    # Calculate how many bags of chips Jeremy bought
    jeremy_bags = 3

    # Calculate how many bags of chips are left to buy
    remaining_bags = 10 - jeremy_bags - 4

    # Divide the remaining bags evenly between Stacy and Emily
    emily_bags = remaining_bags / 2

    result = emily_bags
    return result

print(solution())