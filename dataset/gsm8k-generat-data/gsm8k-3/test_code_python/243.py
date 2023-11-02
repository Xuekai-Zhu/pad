def solution():
    """Mr. Lu owns a computer store. For last month, half of their sales are laptops, one-third are netbooks, and the rest are desktop computers. If Mr. Lu's store was able to sell a total of 72 computers, how many of them are desktop computers?"""
    # Calculate the number of laptops sold
    laptops_sold = 0.5 * 72

    # Calculate the number of netbooks sold
    netbooks_sold = 1/3 * 72

    # Calculate the number of desktops sold
    desktops_sold = 72 - laptops_sold - netbooks_sold

    # Display the number of desktops sold
    result = desktops_sold
    return result

print(solution())