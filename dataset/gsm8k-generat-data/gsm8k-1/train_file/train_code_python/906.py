def solution():
    """A store received 20 pallets of paper products to stock. Half the pallets were paper towels, a quarter were tissues, and a fifth were paper plates. The rest were paper cups. How many pallets of paper cups did the store receive?"""
    total_pallets = 20
    paper_towel_pallets = total_pallets / 2
    tissue_pallets = total_pallets / 4
    paper_plate_pallets = total_pallets / 5
    paper_cup_pallets = total_pallets - paper_towel_pallets - tissue_pallets - paper_plate_pallets
    result = paper_cup_pallets
    return result

print(solution())