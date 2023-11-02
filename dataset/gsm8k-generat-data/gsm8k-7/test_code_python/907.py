def solution():
    total_pallets = 20
    paper_towels = total_pallets / 2
    tissues = total_pallets / 4
    paper_plates = total_pallets / 5

    # Calculate the total number of pallets of paper products that are not paper towels, tissues, or paper plates
    remaining_pallets = total_pallets - paper_towels - tissues - paper_plates

    # Calculate the number of pallets of paper cups
    num_paper_cups = remaining_pallets
    result = num_paper_cups
    return result

print(solution())