def solution():
    # Calculate the number of laptops sold
    laptops = (1/2) * 72
    # Calculate the number of netbooks sold
    netbooks = (1/3) * 72
    # Calculate the number of desktop computers sold
    desktops = 72 - laptops - netbooks
    result = desktops
    return result

print(solution())