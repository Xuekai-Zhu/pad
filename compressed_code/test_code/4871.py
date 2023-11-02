def solution():
    
    march_sales = 8800
    february_sales = march_sales * 0.25
    january_sales = february_sales / 2
    total_sales = january_sales + february_sales + march_sales
    result = total_sales
    return result

print(solution())