def solution():
    pens = 3
    notebooks = 4
    folders = 2
    pen_cost = 1
    notebook_cost = 3
    folder_cost = 5
    total_cost = pens * pen_cost + notebooks * notebook_cost + folders * folder_cost
    payment = 50
    change = payment - total_cost
    
    return change

print(solution())