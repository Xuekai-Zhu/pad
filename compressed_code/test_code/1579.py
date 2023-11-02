def solution():
    
    total_books = 250
    tuesday_taken = 120
    wednesday_returned = 35
    thursday_taken = 15
    remaining_books = total_books - tuesday_taken + wednesday_returned - thursday_taken
    result = remaining_books
    return result

print(solution())