def solution():
    
    bag_weight = 20
    cookie_weight = 9
    num_bags = 6
    num_cookies = 4 * num_bags
    total_weight = (bag_weight * num_bags + cookie_weight * num_cookies) / 16
    result = total_weight
    return result

print(solution())