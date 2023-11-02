def solution():
    num_students = 30  # The third grade class has 30 students
    pens_per_student = 5
    notebooks_per_student = 3
    binders_per_student = 1
    highlighters_per_student = 2

    # Calculate the total number of each item needed
    total_pens = num_students * pens_per_student
    total_notebooks = num_students * notebooks_per_student
    total_binders = num_students * binders_per_student
    total_highlighters = num_students * highlighters_per_student

    # Calculate the total cost of all items before the discount
    pens_cost = total_pens * 0.50
    notebooks_cost = total_notebooks * 1.25
    binders_cost = total_binders * 4.25
    highlighters_cost = total_highlighters * 0.75
    total_cost = pens_cost + notebooks_cost + binders_cost + highlighters_cost

    # Apply the teacher discount
    total_cost -= 100

    result = total_cost
    return result

print(solution())