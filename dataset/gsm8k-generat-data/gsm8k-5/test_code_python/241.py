def solution():
    total_sales = 72  # The store sold a total of 72 computers
    laptops = total_sales / 2  # Half of the sales are laptops
    netbooks = total_sales / 3  # One-third of the sales are netbooks
    desktops = total_sales - laptops - netbooks  # The rest of the sales are desktops
    result = desktops
    return result

print(solution())