def solution():
    """Carl is having a party on Saturday and is inviting 15 guests. He would like to make sure everyone, including himself, has at least 2 glasses of punch. Each glass holds 12 ounces of punch. How many ounces of punch does he need to buy for the party?"""
    # Define the number of guests and glasses per guest
    guests = 15
    glasses_per_guest = 2

    # Define the size of each glass in ounces
    glass_size = 12

    # Calculate the total amount of punch needed
    total_punch = guests * glasses_per_guest * glass_size

    result = total_punch
    return result

print(solution())