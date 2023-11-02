def solution():
    """Bob picked 450 apples for his entire family to eat. There are 33 children in his family, and each of them ate 10 apples. If every adult ate 3 apples apiece, how many adults are in his family?"""
    # Calculate the total number of apples eaten by the children
    children_apples = 33 * 10

    # Calculate the remaining number of apples for the adults
    adult_apples = 450 - children_apples

    # Calculate the number of adults in Bob's family
    adults = adult_apples // 3

    # Display the number of adults
    result = adults
    return result

print(solution())