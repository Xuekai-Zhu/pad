def solution():
    """Dawn, Lydia, and Donna have a total of 200 bananas. Dawn has 40 more bananas than Lydia. If Lydia has 60 bananas, how many bananas does Donna have?"""
    # Define the number of bananas Lydia has
    lydia_bananas = 60

    # Define the difference in number of bananas between Dawn and Lydia
    dawn_lydia_diff = 40

    # Calculate the number of bananas Dawn has
    dawn_bananas = lydia_bananas + dawn_lydia_diff

    # Calculate the number of bananas Donna has
    donna_bananas = 200 - (lydia_bananas + dawn_bananas)

    # Return the result
    result = donna_bananas
    return result

print(solution())