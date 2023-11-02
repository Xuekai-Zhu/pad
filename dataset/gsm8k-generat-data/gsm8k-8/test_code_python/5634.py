def solution():
    # Calculate the total sales of the paper cover version
    paper_cover_sales = 32000 * 0.20

    # Calculate the author's earnings from the paper cover version
    paper_cover_earnings = paper_cover_sales * 0.06

    # Calculate the total sales of the hardcover version
    hardcover_sales = 15000 * 0.40

    # Calculate the author's earnings from the hardcover version
    hardcover_earnings = hardcover_sales * 0.12

    # Calculate the total earnings of the author
    total_earnings = paper_cover_earnings + hardcover_earnings
    result = total_earnings
    return result

print(solution())