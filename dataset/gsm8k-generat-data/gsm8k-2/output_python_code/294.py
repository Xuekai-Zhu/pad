def solution():
    """Pam has some bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. Gerald's bags have 40 apples each. If Pam has 1200 apples in total, how many bags of apples does she have?"""
    gerald_bag_size = 40
    pam_bag_size = 3 * gerald_bag_size
    total_apples = 1200
    total_pam_bags = total_apples / pam_bag_size
    result = total_pam_bags
    return result

print(solution())