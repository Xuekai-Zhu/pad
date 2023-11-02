def solution():
    
    total_pallets = 20
    paper_towels = total_pallets * 0.5
    tissues = total_pallets * 0.25
    paper_plates = total_pallets * 0.2
    paper_cups = total_pallets - paper_towels - tissues - paper_plates
    result = paper_cups
    return result

print(solution())