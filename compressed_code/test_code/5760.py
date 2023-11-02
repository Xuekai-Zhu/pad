def solution():
    
    book_cost = 12
    num_students = 30
    total_book_cost = book_cost * num_students
    school_fund = 320
    if total_book_cost > school_fund:
        out_of_pocket_cost = total_book_cost - school_fund
    else:
        out_of_pocket_cost = 0
    result = out_of_pocket_cost
    return result

print(solution())