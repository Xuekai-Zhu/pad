def solution():
    num_gerald_bags = 3
    gerald_bag_size = 40
    num_pam_bags = 10

    # Calculate the total number of apples in Gerald's bags
    total_gerald_apples = num_gerald_bags * gerald_bag_size

    # Calculate the total number of apples in Pam's bags
    total_pam_apples = total_gerald_apples * num_pam_bags

    result = total_pam_apples
    return result

print(solution())