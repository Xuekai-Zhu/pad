def solution():
    # Amount already saved
    saved = 10
    
    # Cost of clarinet
    clarinet_cost = 90
    
    # Price of each book
    book_price = 5
    
    # Total books sold to reach the goal
    total_books = 0
    
    while saved < clarinet_cost:
        # Selling a book
        saved += book_price
        total_books += 1
        
        # If halfway towards goal and savings are lost
        if saved >= clarinet_cost/2:
            saved = 0
            
    # Selling remaining books to reach goal
    total_books += (clarinet_cost - saved) / book_price
    
    result = total_books
    return result

print(solution())