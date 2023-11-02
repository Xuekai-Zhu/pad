def solution():
    # Calculate the total earnings from paper cover version sales
    paper_sales = 32000 * 0.20
    paper_earnings = 0.06 * paper_sales

    # Calculate the total earnings from hardcover version sales
    hardcover_sales = 15000 * 0.40
    hardcover_earnings = 0.12 * hardcover_sales

    # Calculate the total earnings for the author
    total_earnings = paper_earnings + hardcover_earnings
    result = total_earnings
    return result

print(solution())