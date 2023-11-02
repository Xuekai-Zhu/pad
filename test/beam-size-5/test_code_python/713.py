def solution():
    
    pencil_cost = 0.5
    eraser_cost = 0.25
    num_pencils = 6
    num_erasers = 8
    total_cost = (pencil_cost * num_pencils) + (eraser_cost * num_erasers)
    change = 10 - total_cost
    result = change
    return result

print(solution())