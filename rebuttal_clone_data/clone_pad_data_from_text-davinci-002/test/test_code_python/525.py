def solution():
    paper_products = 20
    paper_towels = paper_products / 2
    tissues = paper_products / 4
    paper_plates = paper_products / 5
    paper_cups = paper_products - paper_towels - tissues - paper_plates
    result = paper_cups
    
    return result

print(solution())