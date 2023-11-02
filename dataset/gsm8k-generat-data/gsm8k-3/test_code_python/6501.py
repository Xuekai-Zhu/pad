def solution():
    """Amara had 100 pieces of clothing but started donating her clothes to others. She donated 5 to one orphanage home and triple that to another orphanage home. If she decides to throw away 15 of her old clothes, how many pieces of clothing does she have remaining?"""
    # Define the initial number of clothes
    num_clothes = 100

    # Donate 5 clothes to one orphanage
    num_clothes -= 5

    # Donate triple the amount to another orphanage
    num_clothes -= 5 * 3

    # Throw away 15 of her old clothes
    num_clothes -= 15

    # Display the remaining number of clothes
    result = num_clothes
    return result

print(solution())