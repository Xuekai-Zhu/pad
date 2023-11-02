def solution():
    """Sally teaches elementary school and is given $320 to spend on books for her students. A reading book costs $12 and there are 30 students in her class. Unfortunately, if the money she is given by the school to pay for books is not sufficient, she will need to pay the rest out of pocket. How much money does Sally need to pay out of pocket, to buy every student a reading book?"""
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