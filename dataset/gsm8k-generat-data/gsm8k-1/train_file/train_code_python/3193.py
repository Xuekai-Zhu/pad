def solution():
    """At a birthday party, 30% of the guests are married, 50% are single, and the rest are children. If there are 1000 guests, how many more married people are there than children?"""
    total_guests = 1000
    married_percent = 0.3
    single_percent = 0.5
    children_percent = 1 - married_percent - single_percent
    married_guests = married_percent * total_guests
    children_guests = children_percent * total_guests
    difference = married_guests - children_guests
    result = difference
    return result

print(solution())