def solution():
    """Out of the 120 people who attended the party, 1/3 are men while half are women. The rest are children. How many children attended the party?"""
    # Calculate the number of men
    men = 120 * (1/3)

    # Calculate the number of women
    women = 120 * (1/2)

    # Calculate the number of children
    children = 120 - men - women

    # Display the number of children
    result = children
    return result

print(solution())