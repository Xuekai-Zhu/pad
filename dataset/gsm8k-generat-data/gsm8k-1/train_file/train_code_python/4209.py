def solution():
    """For the gala luncheon planning committee, Margaret wants to serve chicken salad sandwiches using mini croissants. She wants there to be enough food that each person on the committee can have 2 sandwiches each. Her bakery offers 12 minis croissants for $8.00. There are 24 people on the committee. How much will she spend on croissants?"""
    croissants_per_pack = 12
    cost_per_pack = 8.00
    sandwiches_per_person = 2
    total_people = 24
    total_sandwiches = sandwiches_per_person * total_people
    packs_needed = total_sandwiches // croissants_per_pack + 1
    cost = packs_needed * cost_per_pack
    result = cost
    return result

print(solution())