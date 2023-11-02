def solution():
    """A large gathering occurred at the town hall with 200 people participating. 100 people decided to have a snack, and then 20 new outsiders joined in to have a snack. Half of these snack eaters got full and left. 10 new outsiders came to have snacks, too. 30 more snack eaters got their fill and left. Then half of the remaining snack eaters left later on. How many snack eaters are left?"""
    # Initialize the number of snack eaters
    snack_eaters = 100

    # 20 new outsiders join in and half of them get full and leave
    snack_eaters = snack_eaters + 20 - 10

    # 30 more snack eaters get their fill and leave
    snack_eaters = snack_eaters - 30

    # Half of the remaining snack eaters leave
    snack_eaters = snack_eaters // 2

    # Calculate the number of snack eaters left
    result = snack_eaters
    return result

print(solution())