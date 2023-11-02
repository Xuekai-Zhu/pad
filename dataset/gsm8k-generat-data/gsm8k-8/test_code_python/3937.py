def solution():
    # Define prices of each item
    bracelet_price = 4
    keychain_price = 5
    book_price = 3

    # Calculate Paula's total cost
    paula_cost = 2*bracelet_price + keychain_price

    # Calculate Olive's total cost
    olive_cost = bracelet_price + book_price

    # Calculate total cost for both
    total_cost = paula_cost + olive_cost
    result = total_cost
    return result

print(solution())