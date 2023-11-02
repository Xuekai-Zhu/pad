def solution():
    total_units = 20
    defective_units = 5
    units_sold_A = 3
    units_sold_C = 7
    units_sold_B = total_units - defective_units - units_sold_A - units_sold_C
    result = units_sold_B
    return result

print(solution())