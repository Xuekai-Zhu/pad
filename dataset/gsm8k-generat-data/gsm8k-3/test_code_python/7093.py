def solution():
    """Carl is having a party on Saturday and is inviting 15 guests. He would like to make sure everyone, including himself, has at least 2 glasses of punch. Each glass holds 12 ounces of punch. How many ounces of punch does he need to buy for the party?"""
    # Define the number of guests and glasses per guest
    GUESTS = 15
    GLASSES_PER_GUEST = 2

    # Define the size of each glass in ounces
    GLASS_SIZE = 12

    # Calculate the total ounces of punch needed
    total_ounces = GUESTS * GLASSES_PER_GUEST * GLASS_SIZE

    # Display the total ounces of punch needed
    result = total_ounces
    return result

print(solution())