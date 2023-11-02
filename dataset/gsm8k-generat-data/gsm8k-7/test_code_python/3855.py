def solution():
    num_boxes = 30
    packs_per_box = 40
    diapers_per_pack = 160
    price_per_diaper = 5

    # Calculate the total number of diapers that Meadow orders each week
    total_diapers_per_week = num_boxes * packs_per_box * diapers_per_pack

    # Calculate the total amount of money Meadow makes each week
    total_money_per_week = total_diapers_per_week * price_per_diaper

    # Calculate the total amount of money Meadow makes in a year (assuming 52 weeks in a year)
    total_money_per_year = total_money_per_week * 52
    result = total_money_per_year
    return result

print(solution())