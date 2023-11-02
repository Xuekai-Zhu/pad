def solution():
    """Dawn, Lydia, and Donna have a total of 200 bananas. Dawn has 40 more bananas than Lydia. If Lydia has 60 bananas, how many bananas does Donna have?"""
    # Determine the number of bananas Dawn has
    dawn_bananas = 60 + 40

    # Determine the number of bananas Donna has
    donna_bananas = 200 - (dawn_bananas + 60)

    # Display the number of bananas Donna has
    result = donna_bananas
    return result

print(solution())