def solution():
    """An author of a book got 6% of the total sales of the paper cover version of his books and 12% of the total sales of the hardcover version. If 32,000 copies of the paper cover version were sold at $0.20 each and 15,000 copies of the hardcover version were sold at $0.40 each, how much did the author earn?"""
    paper_copies = 32000
    hardcover_copies = 15000
    paper_price = 0.20
    hardcover_price = 0.40

    paper_sales = paper_copies * paper_price
    hardcover_sales = hardcover_copies * hardcover_price

    paper_profit = paper_sales * 0.06
    hardcover_profit = hardcover_sales * 0.12

    total_profit = paper_profit + hardcover_profit
    result = total_profit
    return result

print(solution())