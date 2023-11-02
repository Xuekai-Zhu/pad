def solution():
    """Alicia's clothes have to be sent to the dry cleaners weekly. Her weekly drop-off includes 5 blouses, 2 pants and 1 skirt.
    If they charge her $5.00 per blouse, $6.00 per skirt and $8.00 per pair of pants, how much does she spend on dry-cleaning in 5 weeks?"""
    blouses_per_week = 5
    pants_per_week = 2
    skirts_per_week = 1
    weeks = 5
    blouse_price = 5
    pant_price = 8
    skirt_price = 6
    total_blouse_price = blouses_per_week * blouse_price * weeks
    total_pant_price = pants_per_week * pant_price * weeks
    total_skirt_price = skirts_per_week * skirt_price * weeks
    total_price = total_blouse_price + total_pant_price + total_skirt_price
    result = total_price
    return result

print(solution())