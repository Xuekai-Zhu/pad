def solution():
    paper_cover_sold = 32000
    paper_cover_price = 0.20
    hardcover_sold = 15000
    hardcover_price = 0.40
    paper_cover_royalty_rate = 0.06
    hardcover_royalty_rate = 0.12

    # Calculate the total revenue from paper cover sales
    paper_cover_revenue = paper_cover_sold * paper_cover_price

    # Calculate the total revenue from hardcover sales
    hardcover_revenue = hardcover_sold * hardcover_price

    # Calculate the author's earnings from paper cover sales
    paper_cover_earnings = paper_cover_revenue * paper_cover_royalty_rate

    # Calculate the author's earnings from hardcover sales
    hardcover_earnings = hardcover_revenue * hardcover_royalty_rate

    # Calculate the total earnings of the author
    total_earnings = paper_cover_earnings + hardcover_earnings
    result = total_earnings
    return result

print(solution())