def solution():
    """8 jumbo scallops weigh one pound and cost $24.00 a pound. Nate is pairing 2 scallops with a corn bisque as a light summer dinner. He’s cooking for 8 people. How much will the scallops cost?"""
    scallops_per_pound = 8
    price_per_pound = 24
    people = 8
    scallops_per_person = 2
    pounds_needed = (people * scallops_per_person) / scallops_per_pound
    total_cost = pounds_needed * price_per_pound
    result = total_cost
    return result

print(solution())