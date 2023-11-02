def solution():
    # Calculate the number of pupils seated by rectangular tables
    rect_pupils = 7 * 10  # 7 rectangular tables, each seating 10 pupils
    
    # Calculate the number of square tables needed
    square_pupils = 90 - rect_pupils  # total number of pupils - pupils seated by rectangular tables
    square_tables = square_pupils / 4  # each square table seats 4 pupils
    
    result = square_tables
    return result

print(solution())