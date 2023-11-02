def solution():
    
    pen_cost = 3 * 1
    notebook_cost = 4 * 3
    folder_cost = 2 * 5
    total_cost = pen_cost + notebook_cost + folder_cost
    payment = 50
    change = payment - total_cost
    result = change
    return result

print(solution())