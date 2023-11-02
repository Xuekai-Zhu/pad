def solution():
    # Define the number of apples in each bag of Gerald and Pam
    gerald_apples_per_bag = 40
    pam_apples_per_bag = 3 * gerald_apples_per_bag

    # Calculate the total number of bags of Gerald and Pam
    total_bags = (1200 / pam_apples_per_bag) + (1200 / gerald_apples_per_bag)

    result = total_bags
    return result

print(solution())