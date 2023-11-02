def solution():
    gerald_apples_per_bag = 40  # Gerald's bags have 40 apples each
    pam_apples_per_bag = 3 * gerald_apples_per_bag  # Pam's bags have 3 times as many apples as Gerald's bags
    total_apples = 1200  # Pam has 1200 apples in total

    # Calculate the number of bags of apples Pam has
    num_pam_bags = total_apples / pam_apples_per_bag
    result = num_pam_bags
    return result

print(solution())