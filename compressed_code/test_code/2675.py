def solution():
    
    total_flour = 6
    cake_flour = 4
    cake_count = cake_flour / 0.5
    cupcake_flour = total_flour - cake_flour
    cupcake_count = cupcake_flour / (1/5)
    cake_income = cake_count * 2.5
    cupcake_income = cupcake_count * 1
    total_income = cake_income + cupcake_income
    result = total_income
    return result

print(solution())