def solution():
    """ Pam has some bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. Gerald's bags have 40 apples each. If Pam has 1200 apples in total, how many bags of apples does she have? """
    gerald_apples_per_bag = 40
    pam_apples_per_bag = gerald_apples_per_bag * 3
    total_apples = 1200
    total_bags = total_apples / pam_apples_per_bag
    result = total_bags
    return result

print(solution())