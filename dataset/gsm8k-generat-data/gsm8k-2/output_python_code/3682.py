def solution():
    """At a party, there are 50 people. 30% of them are boys. How many girls are at this party?"""
    total_people = 50
    boys = total_people * 0.3
    girls = total_people - boys
    result = girls
    return result

print(solution())