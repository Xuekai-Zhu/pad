def solution():
    """Bob picked 450 apples for his entire family to eat. There are 33 children in his family, and each of them ate 10 apples. If every adult ate 3 apples apiece, how many adults are in his family?"""
    # Define the total number of apples picked
    total_apples = 450

    # Define the number of children in the family
    children = 33

    # Calculate the number of apples consumed by the children
    children_apples = children * 10

    # Calculate the number of apples left for the adults
    adult_apples = total_apples - children_apples

    # Define the number of apples for each adult
    adult_apples_per_person = 3

    # Calculate the number of adults in the family
    adults = adult_apples // adult_apples_per_person

    result = adults
    return result

print(solution())