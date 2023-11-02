def solution():
    """Antoine is having a dinner party and his butcher recommends 1/2 pound of meat per person. If he's inviting 6 people over and the beef tenderloin is $15.00 a pound, how much will this cost him?"""
    pounds_per_person = 0.5
    total_persons = 6
    price_per_pound = 15
    total_pounds = pounds_per_person * total_persons
    total_cost = price_per_pound * total_pounds
    result = total_cost
    return result

print(solution())