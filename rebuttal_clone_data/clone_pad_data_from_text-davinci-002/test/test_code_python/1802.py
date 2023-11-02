def solution():
    cost = 6000
    num_bags = 80
    bag_weight = 50
    new_num_bags = num_bags * 3
    new_bag_weight = bag_weight * 3/5
    new_cost = cost * new_num_bags/num_bags * new_bag_weight/bag_weight
    result = new_cost
    return result

print(solution())