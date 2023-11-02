def solution():
    # Calculate the initial stock of ornamental rings
    initial_stock = 200 / 2  # twice the remaining stock

    # Calculate the number of rings sold after Eliza sells 3/4 of the total stock
    sold_rings = initial_stock * 3/4

    # Calculate the new stock after Eliza's mother buys 300 more rings
    new_stock = sold_rings + initial_stock + 300

    # Calculate the final stock after selling 150 rings
    final_stock = new_stock - 150

    result = final_stock
    return result

print(solution())