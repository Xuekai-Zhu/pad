def solution():
    """Meadow has a business that sells baby diapers to her local townspeople. She orders 30 boxes of diapers containing 40 packs weekly, with each pack having 160 diapers. She sells each diaper for $5. How much money is Meadow making from selling all her diapers?"""
    # Define the number of boxes, packs, and diapers per pack
    BOXES = 30
    PACKS_PER_BOX = 40
    DIAPERS_PER_PACK = 160

    # Calculate the total number of diapers
    total_diapers = BOXES * PACKS_PER_BOX * DIAPERS_PER_PACK

    # Calculate the total revenue from selling all the diapers
    revenue = total_diapers * 5

    # Display the revenue
    result = revenue
    return result

print(solution())