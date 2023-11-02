def solution():
    """
    A large gathering occurred at the town hall with 200 people participating. 100 people decided to have a snack, and then 
    20 new outsiders joined in to have a snack. Half of these snack eaters got full and left. 10 new outsiders came to have 
    snacks, too. 30 more snack eaters got their fill and left. Then half of the remaining snack eaters left later on. How 
    many snack eaters are left?
    """
    total_people = 200
    initial_snackers = 100
    new_snackers_1 = 20
    new_snackers_2 = 10
    leaving_snackers_1 = new_snackers_1 / 2
    remaining_snackers_1 = initial_snackers + new_snackers_1 - leaving_snackers_1
    remaining_snackers_2 = remaining_snackers_1 + new_snackers_2 - 30
    remaining_snackers_3 = remaining_snackers_2 / 2
    result = remaining_snackers_3
    
    return result

print(solution())