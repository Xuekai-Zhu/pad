def solution():
    # Define the number of students and required supplies
    num_students = 30
    pens_per_student = 5
    notebooks_per_student = 3
    binders_per_student = 1
    highlighters_per_student = 2

    # Define the cost of each supply
    pen_cost = 0.50
    notebook_cost = 1.25
    binder_cost = 4.25
    highlighter_cost = 0.75

    # Calculate the total cost of supplies before discount
    total_pen_cost = num_students * pens_per_student * pen_cost
    total_notebook_cost = num_students * notebooks_per_student * notebook_cost
    total_binder_cost = num_students * binders_per_student * binder_cost
    total_highlighter_cost = num_students * highlighters_per_student * highlighter_cost
    total_cost = total_pen_cost + total_notebook_cost + total_binder_cost + total_highlighter_cost

    # Apply the teacher discount and calculate the final cost
    discount = 100
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())