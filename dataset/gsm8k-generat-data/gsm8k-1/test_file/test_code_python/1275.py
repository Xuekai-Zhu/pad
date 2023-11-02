def solution():
    """Avery needs to buy a 3 piece place setting (dinner & salad plate and a bowl) for her holiday dinner. She’s having 12 people over for dinner. If the dinner plates cost $6.00 each and bowls each cost $5.00 and the salad plates cost $4.00, how much will she spend on place settings?"""
    num_people = 12
    dinner_plate_cost = 6
    bowl_cost = 5
    salad_plate_cost = 4
    num_pieces_per_set = 3
    num_sets = num_people * num_pieces_per_set
    total_cost = (num_sets * dinner_plate_cost) + (num_sets * bowl_cost) + (num_sets * salad_plate_cost)
    result = total_cost
    return result

print(solution())