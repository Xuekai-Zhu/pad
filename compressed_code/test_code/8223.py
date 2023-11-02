def solution():
    
    total_units = 20
    defective_units = 5
    non_defective_units = total_units - defective_units
    sold_to_customer_a = 3
    sold_to_customer_c = 7
    sold_to_customer_b = non_defective_units - sold_to_customer_a - sold_to_customer_c
    result = sold_to_customer_b
    return result

print(solution())