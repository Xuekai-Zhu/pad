def solution():
    
    paula_bracelets = 2
    paula_keychains = 1
    olive_bracelets = 1
    olive_coloring_books = 1
    price_per_bracelet = 4
    price_per_keychain = 5
    price_per_coloring_book = 3
    paula_total = (paula_bracelets * price_per_bracelet) + (paula_keychains * price_per_keychain)
    olive_total = (olive_bracelets * price_per_bracelet) + (olive_coloring_books * price_per_coloring_book)
    total_spent = paula_total + olive_total
    result = total_spent
    return result

print(solution())