def solution():
    """One hundred people attended a party. Fifty percent of the attendees are women, thirty-five percent of them are men, and the rest are children. How many children attended the party?"""
    total_people = 100
    women_percent = 50
    men_percent = 35
    children_percent = 100 - women_percent - men_percent
    children_count = (children_percent / 100) * total_people
    result = children_count
    return result

print(solution())