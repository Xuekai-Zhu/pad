def solution():
    months_per_book = 2
    years_writing = 20
    average_earnings = 30000
    
    total_books = years_writing * (12 / months_per_book)
    total_earnings = total_books * average_earnings
    result = total_earnings
    
    return result

print(solution())