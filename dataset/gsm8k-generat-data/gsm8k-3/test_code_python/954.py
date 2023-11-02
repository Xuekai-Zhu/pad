def solution():
    """Pam has 10 bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. If Gerald's bags have 40 apples each, how many apples does Pam have?"""
    # Define the number of apples in each of Gerald's bags
    GERALD_APPLES_PER_BAG = 40

    # Calculate the number of apples in each of Pam's bags
    PAM_APPLES_PER_BAG = 3 * GERALD_APPLES_PER_BAG

    # Calculate the total number of apples Pam has
    total_apples = 10 * PAM_APPLES_PER_BAG

    # Display the total number of apples Pam has
    result = total_apples
    return result

print(solution())