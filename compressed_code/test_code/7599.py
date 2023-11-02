def solution():
    
    book1_cost = 13
    book2_cost = 15
    book3_cost = 10
    book4_cost = 10
    num_books_for_discount = 4
    discount_rate = 0.25

    
    discounted_books_cost = book1_cost + book2_cost - (book1_cost + book2_cost) * discount_rate

    
    total_cost = discounted_books_cost + book3_cost + book4_cost

    
    remaining_shipping_cost = 50 - total_cost
    result = remaining_shipping_cost
    return result

print(solution())