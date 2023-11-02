def solution():
    
    total_units = 20
    defective_units = 5
    non_defective_units = total_units - defective_units
    non_defective_units_sold = 3 + 7
    customer_b_units_sold = non_defective_units - non_defective_units_sold
    result = customer_b_units_sold
    return result

print(solution())