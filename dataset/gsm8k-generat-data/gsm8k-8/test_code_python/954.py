def solution():
    # Define the number of apples in each of Gerald's bags
    ger_apples_per_bag = 40
    
    # Calculate the number of apples in each of Pam's bags
    pam_apples_per_bag = ger_apples_per_bag * 3
    
    # Calculate the total number of apples that Pam has
    pam_total_apples = pam_apples_per_bag * 10
    result = pam_total_apples
    return result

print(solution())