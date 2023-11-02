def solution():
    """Pam has 10 bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. If Gerald's bags have 40 apples each, how many apples does Pam have?"""
    # Define the number of apples in each of Gerald's bags
    gerald_apples_per_bag = 40

    # Calculate the total number of apples in Gerald's bags
    total_gerald_apples = gerald_apples_per_bag * 3 * 10

    # Calculate the total number of apples in Pam's bags
    total_pam_apples = total_gerald_apples

    result = total_pam_apples
    return result

print(solution())