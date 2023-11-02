def solution():
    pepperoni = 30
    sausage = pepperoni + 12
    ham = 2 * pepperoni
    total_meat = pepperoni + sausage + ham
    meat_per_slice = total_meat / 6
    
    result = meat_per_slice
    return result

print(solution())