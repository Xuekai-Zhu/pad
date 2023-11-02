def solution():
    
    num_whale_books = 9
    num_fish_books = 7
    num_magazines = 3
    price_per_book = 11
    price_per_magazine = 1
    
    total_book_cost = (num_whale_books + num_fish_books) * price_per_book
    total_magazine_cost = num_magazines * price_per_magazine
    
    total_cost = total_book_cost + total_magazine_cost
    result = total_cost
    return result

print(solution())