def solution():
    num_apples_per_gerald_bag = 40

    # Calculate the total number of apples in Gerald's bags
    total_gerald_apples = num_apples_per_gerald_bag * 3

    # Calculate the total number of Pam's bags
    total_pam_bags = 1200 / total_gerald_apples
    result = total_pam_bags
    return result

print(solution())