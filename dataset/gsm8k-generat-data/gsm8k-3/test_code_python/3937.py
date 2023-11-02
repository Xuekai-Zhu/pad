def solution():
    """A kiddy gift shop sells bracelets at $4 each, keychains at $5 each, and coloring books at $3 each. Paula and Olive want to buy presents for their friends. Paula buys two bracelets and a keychain, while Olive buys a coloring book and a bracelet.  How much do Paula and Olive spend in total?"""
    # Define the prices of each item
    BRACELET_PRICE = 4
    KEYCHAIN_PRICE = 5
    COLORING_BOOK_PRICE = 3

    # Paula's purchases
    paula_bracelets = 2
    paula_keychains = 1

    # Olive's purchases
    olive_bracelets = 1
    olive_coloring_books = 1

    # Calculate the total cost for Paula and Olive
    paula_cost = (paula_bracelets * BRACELET_PRICE) + (paula_keychains * KEYCHAIN_PRICE)
    olive_cost = (olive_bracelets * BRACELET_PRICE) + (olive_coloring_books * COLORING_BOOK_PRICE)
    total_cost = paula_cost + olive_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())