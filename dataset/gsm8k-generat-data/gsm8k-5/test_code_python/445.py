def solution():
    bag_price = 6.00  # the original price of each bag
    discount_percentage = 75  # the discount percentage
    num_bags = 2  # the number of bags Carla bought

    # Calculate the discounted price of each bag
    discounted_price = bag_price * (1 - discount_percentage/100)

    # Calculate the total cost of the two bags
    total_cost = discounted_price * num_bags
    result = total_cost
    return result

print(solution())