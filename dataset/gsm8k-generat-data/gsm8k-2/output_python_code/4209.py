def solution():
    """For the gala luncheon planning committee, Margaret wants to serve chicken salad sandwiches using mini croissants. She wants there to be enough food that each person on the committee can have 2 sandwiches each. Her bakery offers 12 minis croissants for $8.00. There are 24 people on the committee. How much will she spend on croissants?"""
    sandwiches_per_person = 2
    people_on_committee = 24
    croissants_per_sandwich = 1  # each sandwich needs one mini croissant
    croissants_per_dozen = 12
    cost_per_dozen = 8
    total_sandwiches = sandwiches_per_person * people_on_committee
    total_croissants = total_sandwiches * croissants_per_sandwich
    dozens_needed = total_croissants / croissants_per_dozen

    # rounding up to the nearest whole dozen
    if dozens_needed != int(dozens_needed):
        dozens_needed = int(dozens_needed) + 1

    total_cost = dozens_needed * cost_per_dozen
    result = total_cost
    return result

print(solution())