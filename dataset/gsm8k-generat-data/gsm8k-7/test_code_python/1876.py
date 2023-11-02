def solution():
    # Define variables
    num_expected = 50
    num_extra = 40
    num_gift_bags = 10
    num_average_bags = 20

    # Calculate the total number of visitors
    total_visitors = num_expected + num_extra

    # Calculate the number of gift bags needed for all visitors
    num_all_bags = total_visitors - num_gift_bags

    # Calculate the number of extra bags needed
    num_extra_bags = num_all_bags - num_average_bags

    result = num_extra_bags
    return result

print(solution())