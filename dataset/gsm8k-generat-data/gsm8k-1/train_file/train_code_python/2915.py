def solution():
    """Antoine is having a dinner party and his butcher recommends 1/2 pound of meat per person. If he's inviting 6 people over and the beef tenderloin is $15.00 a pound, how much will this cost him?"""
    meat_per_person = 0.5
    num_people = 6
    price_per_pound = 15.00
    total_meat = meat_per_person * num_people
    total_cost = total_meat * price_per_pound
    result = total_cost
    return result

print(solution())