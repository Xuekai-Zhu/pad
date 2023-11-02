def solution():
    bracelet_price = 4
    keychain_price = 5
    coloring_book_price = 3
    paula_bracelets = 2
    paula_keychains = 1
    paula_total = paula_bracelets * bracelet_price + paula_keychains * keychain_price
    olive_bracelets = 1
    olive_coloring_books = 1
    olive_total = olive_bracelets * bracelet_price + olive_coloring_books * coloring_book_price 
    total_spent = paula_total + olive_total
    result = total_spent
    return result

print(solution())