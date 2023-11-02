def solution():
    total_units = 20
    defective_units = 5
    non_defective_units = total_units - defective_units
    customer_a_units = 3
    customer_c_units = 7
    units_sold = customer_a_units + customer_c_units
    units_sold_to_b = non_defective_units - units_sold
    result = units_sold_to_b
    return result

print(solution())