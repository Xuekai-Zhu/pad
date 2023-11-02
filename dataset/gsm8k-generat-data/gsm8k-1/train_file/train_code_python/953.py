def solution():
    """Pam has 10 bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. If Gerald's bags have 40 apples each, how many apples does Pam have?"""
    gerald_apples_per_bag = 40
    pam_bags = 10
    gerald_bags_for_pam_bag = 3
    pam_apples_per_bag = gerald_apples_per_bag * gerald_bags_for_pam_bag
    pam_total_apples = pam_apples_per_bag * pam_bags
    result = pam_total_apples
    return result

print(solution())