def solution():
    
    total_pallets = 20
    paper_towel_pallets = total_pallets / 2
    tissue_pallets = total_pallets / 4
    paper_plate_pallets = total_pallets / 5
    paper_cup_pallets = total_pallets - paper_towel_pallets - tissue_pallets - paper_plate_pallets
    result = paper_cup_pallets
    return result

print(solution())