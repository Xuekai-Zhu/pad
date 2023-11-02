def solution():
    # Calculate net increase in the number of bicycles in stock over three days
    starting_stock = 0
    ending_stock = starting_stock + 10 + 15 - 12 + 8 - 9 + 11  # calculate the ending stock after all transactions
    net_increase = ending_stock - starting_stock  # calculate net increase in stock
    result = net_increase
    return result

print(solution())