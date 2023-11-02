def solution():
    """Mr. Lu owns a computer store. For last month, half of their sales are laptops, one-third are netbooks, and the rest are desktop computers. If Mr. Lu's store was able to sell a total of 72 computers, how many of them are desktop computers?"""
    total_sales = 72
    laptop_sales = total_sales / 2
    netbook_sales = total_sales / 3
    desktop_sales = total_sales - laptop_sales - netbook_sales
    result = desktop_sales
    return result

print(solution())