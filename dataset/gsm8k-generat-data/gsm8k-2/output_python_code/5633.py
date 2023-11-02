def solution():
    """An author of a book got 6% of the total sales of the paper cover version of his books and 12% of the total sales of the hardcover version. If 32,000 copies of the paper cover version were sold at $0.20 each and 15,000 copies of the hardcover version were sold at $0.40 each, how much did the author earn?"""
    paper_sales = 32000 * 0.20
    hardcover_sales = 15000 * 0.40
    paper_royalty = paper_sales * 0.06
    hardcover_royalty = hardcover_sales * 0.12
    total_royalty = paper_royalty + hardcover_royalty
    result = total_royalty
    return result

print(solution())