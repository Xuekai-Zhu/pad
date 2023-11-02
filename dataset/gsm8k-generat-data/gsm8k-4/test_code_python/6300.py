def solution():
    """Bennett sells window screens. He sold twice as many window screens in February as he sold last month. In February, Bennett sold a fourth of what he sold in March. If Bennet sold 8800 window screens in March, how many screens did Bennett sell from January to March?"""
    # Calculate the number of screens sold in March
    march_sales = 8800

    # Calculate the number of screens sold in February
    february_sales = march_sales / 4

    # Calculate the number of screens sold in January
    january_sales = february_sales / 2

    # Calculate the total number of screens sold from January to March
    total_sales = january_sales + february_sales + march_sales

    result = total_sales
    return result

print(solution())