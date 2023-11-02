def solution():
    """Sally teaches elementary school and is given $320 to spend on books for her students. A reading book costs $12 and there are 30 students in her class. Unfortunately, if the money she is given by the school to pay for books is not sufficient, she will need to pay the rest out of pocket. How much money does Sally need to pay out of pocket, to buy every student a reading book?"""
    # Define the budget given by the school and the cost of a reading book
    budget = 320
    book_cost = 12

    # Calculate the total cost of buying a reading book for each student
    total_cost = book_cost * 30

    # If the budget is enough, no need to pay out of pocket
    if budget >= total_cost:
        out_of_pocket = 0
    else:
        out_of_pocket = total_cost - budget

    result = out_of_pocket
    return result

print(solution())