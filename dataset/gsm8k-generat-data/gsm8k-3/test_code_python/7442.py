def solution():
    """Sally teaches elementary school and is given $320 to spend on books for her students. A reading book costs $12 and there are 30 students in her class. Unfortunately, if the money she is given by the school to pay for books is not sufficient, she will need to pay the rest out of pocket. How much money does Sally need to pay out of pocket, to buy every student a reading book?"""
    # Define the cost of one reading book and the number of students
    BOOK_COST = 12
    NUM_STUDENTS = 30

    # Calculate the total cost of buying 30 reading books
    total_cost = BOOK_COST * NUM_STUDENTS

    # Check if the total cost is greater than the budget
    if total_cost <= 320:
        remaining_budget = 320 - total_cost
        out_of_pocket = 0
    else:
        remaining_budget = 0
        out_of_pocket = total_cost - 320

    # Display the amount Sally needs to pay out of pocket
    result = out_of_pocket
    return result

print(solution())