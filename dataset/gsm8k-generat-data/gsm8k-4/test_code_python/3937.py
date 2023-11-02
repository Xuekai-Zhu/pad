def solution():
    """A kiddy gift shop sells bracelets at $4 each, keychains at $5 each, and coloring books at $3 each. Paula and Olive want to buy presents for their friends. Paula buys two bracelets and a keychain, while Olive buys a coloring book and a bracelet. How much do Paula and Olive spend in total?"""
    # Define the prices of the items
    bracelet_price = 4
    keychain_price = 5
    book_price = 3

    # Calculate Paula's total cost
    paula_cost = (2 * bracelet_price) + keychain_price

    # Calculate Olive's total cost
    olive_cost = bracelet_price + book_price

    # Calculate the total cost of the presents
    total_cost = paula_cost + olive_cost

    # return the result
    result = total_cost
    return result

print(solution())