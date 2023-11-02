def solution():
    """Jackson is buying school supplies for his third grade class, which has 30 students. Each student needs 5 pens, 3 notebooks, 1 binder and 2 highlighters. Pens cost $0.50, notebooks cost $1.25, binders cost $4.25, and highlighters cost $0.75. If Jackson gets a $100 teacher discount, how much does he spend on school supplies?"""
    # Define the number of students and the required supplies per student
    num_students = 30
    pens_per_student = 5
    notebooks_per_student = 3
    binders_per_student = 1
    highlighters_per_student = 2

    # Define the prices of each supply
    pen_price = 0.5
    notebook_price = 1.25
    binder_price = 4.25
    highlighter_price = 0.75

    # Calculate the total cost of supplies before discount
    total_cost = (pens_per_student * num_students * pen_price) + (notebooks_per_student * num_students * notebook_price) + (binders_per_student * num_students * binder_price) + (highlighters_per_student * num_students * highlighter_price)

    # Apply the teacher discount
    total_cost -= 100

    # return the result
    result = total_cost
    return result

print(solution())