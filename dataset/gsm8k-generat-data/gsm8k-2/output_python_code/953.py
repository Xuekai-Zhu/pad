def solution():
    """Pam has 10 bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. If Gerald's bags have 40 apples each, how many apples does Pam have?"""
    gerald_apples_per_bag = 40
    pam_bags = 10
    gerald_bags = pam_bags * 3
    gerald_apples = gerald_bags * gerald_apples_per_bag
    pam_apples = gerald_apples
    result = pam_apples
    return result

print(solution())