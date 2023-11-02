def solution():
    """A large gathering occurred at the town hall with 200 people participating. 100 people decided to have a snack, and then 20 new outsiders joined in to have a snack. Half of these snack eaters got full and left. 10 new outsiders came to have snacks, too. 30 more snack eaters got their fill and left. Then half of the remaining snack eaters left later on. How many snack eaters are left?"""
    total_people = 200
    initial_snack_eaters = 100
    new_snack_eaters = 20
    half_new_snack_eaters = new_snack_eaters / 2
    remaining_snack_eaters = initial_snack_eaters + new_snack_eaters - half_new_snack_eaters
    more_new_snack_eaters = 10
    total_snack_eaters = remaining_snack_eaters + more_new_snack_eaters
    leaving_snack_eaters = 30
    remaining_snack_eaters -= leaving_snack_eaters
    remaining_snack_eaters /= 2
    result = remaining_snack_eaters
    return result

print(solution())