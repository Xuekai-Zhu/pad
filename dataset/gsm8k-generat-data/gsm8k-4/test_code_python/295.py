def solution():
    """Pam has some bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. Gerald's bags have 40 apples each. If Pam has 1200 apples in total, how many bags of apples does she have?"""
    # Define the number of apples in each of Gerald's bags
    ger_apples_per_bag = 40

    # Calculate the number of apples in all of Gerald's bags
    ger_total_apples = ger_apples_per_bag * (3 + 1 + 1) # 3 + 1 + 1 = 5 bags

    # Calculate the number of apples in all of Pam's bags
    total_apples = 1200

    # Calculate the number of bags Pam has
    pam_bags = total_apples / ger_total_apples

    # Round up to the nearest whole number of bags
    result = round(pam_bags)
    return result

print(solution())