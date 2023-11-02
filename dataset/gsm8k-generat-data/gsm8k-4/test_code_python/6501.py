def solution():
    """Amara had 100 pieces of clothing but started donating her clothes to others. She donated 5 to one orphanage home and triple that to another orphanage home. If she decides to throw away 15 of her old clothes, how many pieces of clothing does she have remaining?"""
    # Define the initial number of clothing pieces
    clothing_pieces = 100

    # Donate 5 to one orphanage home
    clothing_pieces -= 5

    # Donate triple that to another orphanage home
    clothing_pieces -= (5 * 3)

    # Throw away 15 of her old clothes
    clothing_pieces -= 15

    # return the result
    result = clothing_pieces
    return result

print(solution())