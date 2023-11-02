def solution():
    initial_price = 400
    cost_reduction = 15
    cost_increase = 40
    book_price = initial_price - (initial_price * (cost_reduction/100))
    final_price = book_price + (book_price * (cost_increase/100))
    result = final_price
    
    return result

print(solution())