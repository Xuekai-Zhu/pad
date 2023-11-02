def solution():
    """Pam has some bags of apples. Each of her bags has as many apples as 3 of Gerald's bags. Gerald's bags have 40 apples each. If Pam has 1200 apples in total, how many bags of apples does she have?"""
    # Define the number of apples in each of Gerald's bags
    GERALD_APPLES_PER_BAG = 40

    # Calculate the number of bags Pam has
    pam_bags = 1200 / (3 * GERALD_APPLES_PER_BAG)

    # Display the number of bags Pam has
    result = pam_bags
    return result

print(solution())