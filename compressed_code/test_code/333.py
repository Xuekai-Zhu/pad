def solution():
    
    manuscript_pages = 400
    num_copies = 10
    copy_cost = manuscript_pages * 0.05
    bound_cost = 5.00
    total_cost = (copy_cost + bound_cost) * num_copies
    result = total_cost
    return result

print(solution())