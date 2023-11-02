def solution():
    gerald_bag_capacity = 40  # Gerald's bags have 40 apples each
    pam_bag_capacity = 3 * gerald_bag_capacity  # Each of Pam's bags has 3 times as many apples as Gerald's bags
    pam_bags = 10  # Pam has 10 bags of apples

    # Calculate the total number of apples Pam has
    total_apples = pam_bags * pam_bag_capacity
    result = total_apples
    return result

print(solution())