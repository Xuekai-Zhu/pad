def solution():
    """Max is planning a vacation for 8 people. The Airbnb rental costs $3200. They also plan on renting a car that will cost $800. If they plan on splitting the costs equally, how much will each person’s share be?"""
    total_cost = 3200 + 800
    num_people = 8
    share_per_person = total_cost / num_people
    result = share_per_person
    return result

print(solution())