def solution():
    """Bennett sells window screens. He sold twice as many window screens in February as he sold last month. In February, Bennett sold a fourth of what he sold in March. If Bennet sold 8800 window screens in March, how many screens did Bennett sell from January to March?"""
    march_sales = 8800
    february_sales = march_sales * 0.25
    january_sales = february_sales / 2
    total_sales = january_sales + february_sales + march_sales
    result = total_sales
    return result

print(solution())