def solution():
    total_pallets = 20  # The store received 20 pallets in total
    paper_towel_pallets = total_pallets / 2  # Half the pallets were paper towels
    tissue_pallets = total_pallets / 4  # A quarter of the pallets were tissues
    paper_plate_pallets = total_pallets / 5  # A fifth of the pallets were paper plates

    # Calculate the number of pallets of paper cups
    paper_cup_pallets = total_pallets - (paper_towel_pallets + tissue_pallets + paper_plate_pallets)
    result = paper_cup_pallets
    return result

print(solution())