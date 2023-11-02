def solution():
    """Jaynie wants to make leis for the graduation party.  It will take 2 and half dozen plumeria flowers to make 1 lei.  If she wants to make 4 leis, how many plumeria flowers must she pick from the trees in her yard?"""
    # Define the number of flowers needed to make one lei
    FLOWERS_PER_LEI = 2.5 * 12

    # Define the number of leis Jaynie wants to make
    LEIS = 4

    # Calculate the total number of flowers needed
    total_flowers = FLOWERS_PER_LEI * LEIS

    # Display the total number of flowers Jaynie needs to pick
    result = total_flowers
    return result

print(solution())