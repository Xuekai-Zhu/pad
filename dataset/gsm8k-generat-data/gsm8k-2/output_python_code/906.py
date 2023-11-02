def solution():
    """A store received 20 pallets of paper products to stock. Half the pallets were paper towels, a quarter were tissues, and a fifth were paper plates. The rest were paper cups. How many pallets of paper cups did the store receive?"""
    total_pallets = 20
    paper_towels = total_pallets * 0.5
    tissues = total_pallets * 0.25
    paper_plates = total_pallets * 0.2
    paper_cups = total_pallets - paper_towels - tissues - paper_plates
    result = paper_cups
    return result

print(solution())