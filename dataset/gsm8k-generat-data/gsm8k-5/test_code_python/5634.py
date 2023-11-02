def solution():
    paper_cover_price = 0.2  # Price per paper cover book sold
    hardcover_price = 0.4  # Price per hardcover book sold
    paper_cover_sales = 32000  # Number of paper cover books sold
    hardcover_sales = 15000  # Number of hardcover books sold
    paper_cover_percentage = 0.06  # Percentage earned by author from paper cover sales
    hardcover_percentage = 0.12  # Percentage earned by author from hardcover sales

    # Calculate earnings from paper cover sales
    paper_cover_earnings = paper_cover_sales * paper_cover_price * paper_cover_percentage

    # Calculate earnings from hardcover sales
    hardcover_earnings = hardcover_sales * hardcover_price * hardcover_percentage

    # Calculate total earnings
    total_earnings = paper_cover_earnings + hardcover_earnings
    result = total_earnings
    return result

print(solution())