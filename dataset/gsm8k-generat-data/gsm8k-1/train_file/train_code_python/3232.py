def solution():
    """Parker wants to find out what the average percentage of kernels that pop in a bag is. In the first bag he makes, 60 kernels pop and the bag has 75 kernels. In the second bag, 42 kernels pop and there are 50 in the bag. In the final bag, 82 kernels pop and the bag has 100 kernels."""
    bag_one_pop = 60
    bag_one_total = 75
    bag_two_pop = 42
    bag_two_total = 50
    bag_three_pop = 82
    bag_three_total = 100
    
    total_popped = bag_one_pop + bag_two_pop + bag_three_pop
    total_kernels = bag_one_total + bag_two_total + bag_three_total
    average_percent = (total_popped / total_kernels) * 100
    result = average_percent
    return result

print(solution())