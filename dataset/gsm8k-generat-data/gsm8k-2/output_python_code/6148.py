def solution():
    """A bag of chips weighs 20 ounces, and a tin of cookies weighs 9 ounces. If Jasmine buys 6 bags of chips and 4 times as many tins of cookies, how many pounds does she have to carry?"""
    bag_weight = 20
    cookie_weight = 9
    num_bags = 6
    num_cookies = 4 * num_bags
    total_weight = (bag_weight * num_bags + cookie_weight * num_cookies) / 16
    result = total_weight
    return result

print(solution())