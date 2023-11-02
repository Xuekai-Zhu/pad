def solution():
    textbook_price = 45
    discount = 20
    textbooks_needed = 3
    total_discount = textbook_price * (discount / 100)
    total_cost = textbook_price * textbooks_needed
    outside_bookshop_cost = total_cost - (total_discount * textbooks_needed)
    result = outside_bookshop_cost
    
    return result

print(solution())