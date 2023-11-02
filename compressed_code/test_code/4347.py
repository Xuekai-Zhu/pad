def solution():
    
    paper_sales = 32000 * 0.20
    hardcover_sales = 15000 * 0.40
    paper_royalty = paper_sales * 0.06
    hardcover_royalty = hardcover_sales * 0.12
    total_royalty = paper_royalty + hardcover_royalty
    result = total_royalty
    return result

print(solution())