def solution():
    
    pepperoni = 30
    ham = pepperoni * 2
    sausage = pepperoni + 12
    total_meat = pepperoni + ham + sausage
    slices = 6
    pieces_per_slice = total_meat / slices
    result = pieces_per_slice
    return result

print(solution())