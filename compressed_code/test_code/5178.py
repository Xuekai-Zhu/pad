def solution():
    
    starting_books = 98
    checked_out_wed = 43
    returned_thurs = 23
    checked_out_thurs = 5
    returned_fri = 7
    total_books = starting_books - checked_out_wed + returned_thurs - checked_out_thurs + returned_fri
    result = total_books
    return result

print(solution())