def solution():
    # Calculate the initial stock of ornamental rings
    initial_stock = 200 / 2  # Eliza buys twice the remaining stock, so the initial stock = half of what she buys

    # Calculate the total stock after Eliza's purchase
    total_stock = initial_stock + 200  # Eliza buys 200 more rings

    # Calculate the stock after selling 3/4 of the total stock
    remaining_stock = total_stock - (3/4 * total_stock)

    # Calculate the stock after Eliza's mother buys 300 more rings
    remaining_stock += 300

    # Calculate the stock after selling 150 rings
    remaining_stock -= 150

    result = remaining_stock
    return result

print(solution())