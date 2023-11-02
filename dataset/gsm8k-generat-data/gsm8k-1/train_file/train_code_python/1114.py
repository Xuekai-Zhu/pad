def solution():
    """8 jumbo scallops weigh one pound and cost $24.00 a pound. Nate is pairing 2 scallops with a corn bisque as a light summer dinner. He’s cooking for 8 people. How much will the scallops cost?"""
    scallops_per_pound = 8
    cost_per_pound = 24.00
    scallops_per_person = 2
    num_people = 8
    total_scallops_needed = scallops_per_person * num_people
    total_pounds_needed = total_scallops_needed / scallops_per_pound
    total_cost = total_pounds_needed * cost_per_pound
    result = total_cost
    
    return result

print(solution())