def solution():
    """Aunt Angela has 70 jellybeans in a jar. She wants to divide them equally and give them to her 3 nephews and 2 nieces. How many jellybeans did each nephew or niece receive?"""
    jellybeans = 70
    recipients = 3 + 2
    jellybeans_per_person = jellybeans // recipients
    result = jellybeans_per_person
    return result

print(solution())