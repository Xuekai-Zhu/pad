def solution():
    """Bob picked 450 apples for his entire family to eat. There are 33 children in his family, and each of them ate 10 apples. If every adult ate 3 apples apiece, how many adults are in his family?"""
    total_children = 33
    children_apples = total_children * 10
    remaining_apples = 450 - children_apples
    adult_apples = remaining_apples - (total_children * 3)
    adult_count = adult_apples / 3
    result = adult_count
    return result

print(solution())