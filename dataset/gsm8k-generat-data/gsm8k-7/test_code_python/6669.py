def solution():
    num_students = 30
    pens_per_student = 5
    pen_price = 0.5

    notebooks_per_student = 3
    notebook_price = 1.25

    binders_per_student = 1
    binder_price = 4.25

    highlighters_per_student = 2
    highlighter_price = 0.75

    teacher_discount = 100.0

    # Calculate the total number of each item needed for all students
    total_pens = num_students * pens_per_student
    total_notebooks = num_students * notebooks_per_student
    total_binders = num_students * binders_per_student
    total_highlighters = num_students * highlighters_per_student

    # Calculate the total cost of all pens
    total_pen_cost = total_pens * pen_price

    # Calculate the total cost of all notebooks
    total_notebook_cost = total_notebooks * notebook_price

    # Calculate the total cost of all binders
    total_binder_cost = total_binders * binder_price

    # Calculate the total cost of all highlighters
    total_highlighter_cost = total_highlighters * highlighter_price

    # Calculate the total cost of all school supplies before the teacher discount
    total_cost = total_pen_cost + total_notebook_cost + total_binder_cost + total_highlighter_cost

    # Subtract the teacher discount
    total_cost -= teacher_discount

    result = total_cost
    return result

print(solution())