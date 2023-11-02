def solution():
    bracelet_price = 4
    keychain_price = 5
    coloring_book_price = 3

    # Calculate the total cost of Paula's purchases
    paula_cost = (2 * bracelet_price) + keychain_price

    # Calculate the total cost of Olive's purchases
    olive_cost = bracelet_price + coloring_book_price

    # Calculate the total cost of both Paula and Olive's purchases
    total_cost = paula_cost + olive_cost
    result = total_cost
    return result

print(solution())