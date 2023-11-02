def solution():
    pepperoni = 30
    ham = 2 * pepperoni
    sausage = pepperoni + 12
    total_meat = pepperoni + ham + sausage
    slices = 6
    meat_per_slice = total_meat / slices
    result = meat_per_slice
    return result

print(solution())