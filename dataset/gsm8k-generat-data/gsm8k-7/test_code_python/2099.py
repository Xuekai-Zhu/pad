def solution():
    num_books_elmo = 24
    ratio_laura_to_elmo = 1 / 3
    ratio_stu_to_laura = 1 / 2
    
    # Calculate Laura's number of books
    num_books_laura = num_books_elmo * ratio_laura_to_elmo
    
    # Calculate Stu's number of books
    num_books_stu = num_books_laura * ratio_stu_to_laura
    
    result = num_books_stu
    return result

print(solution())