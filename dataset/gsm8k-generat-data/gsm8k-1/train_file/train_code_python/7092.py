def solution():
    """Carl is having a party on Saturday and is inviting 15 guests. He would like to make sure everyone, including himself, has at least 2 glasses of punch. Each glass holds 12 ounces of punch. How many ounces of punch does he need to buy for the party?"""
    guests = 15
    glasses_per_guest = 2
    ounces_per_glass = 12
    total_ounces = guests * glasses_per_guest * ounces_per_glass
    result = total_ounces
    return result

print(solution())