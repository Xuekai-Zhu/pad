def solution():
    """A large gathering occurred at the town hall with 200 people participating. 
    100 people decided to have a snack, and then 20 new outsiders joined in to have a snack. 
    Half of these snack eaters got full and left. 10 new outsiders came to have snacks, too. 
    30 more snack eaters got their fill and left. Then half of the remaining snack eaters left later on. 
    How many snack eaters are left?"""
    
    # Define the initial number of participants and snack eaters
    participants = 200
    snack_eaters = 100

    # Add the new outsiders who join the snack eating group
    snack_eaters += 20

    # Calculate the number of snack eaters who are full and leave
    full_snack_eaters = snack_eaters // 2
    snack_eaters -= full_snack_eaters

    # Add the new outsiders who join the snack eating group
    snack_eaters += 10

    # Calculate the number of snack eaters who are full and leave
    full_snack_eaters += 30
    snack_eaters -= full_snack_eaters

    # Calculate the number of remaining snack eaters
    remaining_snack_eaters = snack_eaters // 2

    # return the result
    result = remaining_snack_eaters
    return result

print(solution())