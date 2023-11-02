def solution():
    num_books = 40
    nephew_books = num_books // 4  # integer division to get number of books given to nephew
    
    # Calculate remaining books after giving some to nephew
    remaining_books = num_books - nephew_books
    
    donated_books = remaining_books // 3  # integer division to get number of books donated to library
    
    # Calculate remaining books after donating some to library
    remaining_books = remaining_books - donated_books
    
    purchased_books = 3
    
    # Calculate total number of books
    total_books = remaining_books + purchased_books
    result = total_books
    return result

print(solution())