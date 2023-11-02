def solution():
    """Mr. Lu owns a computer store. For last month, half of their sales are laptops, one-third are netbooks, and the rest are desktop computers. If Mr. Lu's store was able to sell a total of 72 computers, how many of them are desktop computers?"""
    total_sales = 72
    laptops = total_sales / 2
    netbooks = total_sales / 3
    desktops = total_sales - laptops - netbooks
    result = desktops
    return result

print(solution())