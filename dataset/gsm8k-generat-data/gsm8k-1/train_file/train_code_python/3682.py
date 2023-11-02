def solution():
    """At a party, there are 50 people. 30% of them are boys. How many girls are at this party?"""
    total_people = 50
    percent_boys = 30
    percent_girls = 100 - percent_boys
    girls = (percent_girls / 100) * total_people
    result = girls
    return result

print(solution())