def solution():
    """Meadow has a business that sells baby diapers to her local townspeople. She orders 30 boxes of diapers containing 40 packs weekly, with each pack having 160 diapers. She sells each diaper for $5. How much money is Meadow making from selling all her diapers?"""
    # Define the number of boxes and number of packs
    boxes_per_week = 30
    packs_per_box = 40

    # Define the number of diapers per pack and the price per diaper
    diapers_per_pack = 160
    price_per_diaper = 5

    # Calculate the total number of diapers
    total_diapers = boxes_per_week * packs_per_box * diapers_per_pack

    # Calculate the total revenue from selling all the diapers
    total_revenue = total_diapers * price_per_diaper

    result = total_revenue
    return result

print(solution())