def solution():
    
    num_students = 30
    pens_per_student = 5
    notebooks_per_student = 3
    binders_per_student = 1
    highlighters_per_student = 2
    pen_cost = 0.5
    notebook_cost = 1.25
    binder_cost = 4.25
    highlighter_cost = 0.75
    total_pens = num_students * pens_per_student
    total_notebooks = num_students * notebooks_per_student
    total_binders = num_students * binders_per_student
    total_highlighters = num_students * highlighters_per_student
    total_cost = (total_pens * pen_cost) + (total_notebooks * notebook_cost) + (total_binders * binder_cost) + (total_highlighters * highlighter_cost)
    total_cost -= 100
    result = total_cost
    return result

print(solution())