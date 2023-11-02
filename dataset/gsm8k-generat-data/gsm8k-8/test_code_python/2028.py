def solution():
    # Calculate the initial stock
    initial_stock = 200 / 2
    remaining_stock = initial_stock

    # Calculate the number of rings sold and remaining after selling 3/4 of the total stock
    sold_stock = remaining_stock * 0.75
    remaining_stock = remaining_stock - sold_stock

    # Add the 300 rings bought by Eliza's mother and calculate the remaining stock after selling 150 rings
    remaining_stock = remaining_stock + 300 - 150

    result = remaining_stock
    return result

print(solution())