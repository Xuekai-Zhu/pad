def solution():
    paper_sales = 32000
    paper_price = 0.20
    hardcover_sales = 15000
    hardcover_price = 0.40
    paper_earnings = paper_sales * paper_price * 0.06
    hardcover_earnings = hardcover_sales * hardcover_price * 0.12
    total_earnings = paper_earnings + hardcover_earnings
    result = total_earnings
    
    return result

print(solution())