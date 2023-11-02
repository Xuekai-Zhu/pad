def solution():
    """Mr. Lu owns a computer store. For last month, half of their sales are laptops, one-third are netbooks, and the rest are desktop computers. If Mr. Lu's store was able to sell a total of 72 computers, how many of them are desktop computers?"""
    # Define the total number of computers sold
    total_sales = 72

    # Calculate the number of laptops sold
    laptops = total_sales * 0.5

    # Calculate the number of netbooks sold
    netbooks = total_sales * (1/3)

    # Calculate the number of desktops sold
    desktops = total_sales - laptops - netbooks

    # Return the result
    result = desktops
    return result

print(solution())