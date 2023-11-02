def solution():
    """Bob picked 450 apples for his entire family to eat. There are 33 children in his family, and each of them ate 10 apples. If every adult ate 3 apples apiece, how many adults are in his family?"""
    total_apples = 450
    children = 33
    children_apples = children * 10
    adult_apples = total_apples - children_apples
    adult_apples_per_person = 3
    num_adults = adult_apples // (adult_apples_per_person)
    result = num_adults
    return result

print(solution())