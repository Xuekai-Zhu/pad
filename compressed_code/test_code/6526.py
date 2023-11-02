def solution():
    
    gerald_apples_per_bag = 40
    pam_bags = 10
    gerald_bags_for_pam_bag = 3
    pam_apples_per_bag = gerald_apples_per_bag * gerald_bags_for_pam_bag
    pam_total_apples = pam_apples_per_bag * pam_bags
    result = pam_total_apples
    return result

print(solution())