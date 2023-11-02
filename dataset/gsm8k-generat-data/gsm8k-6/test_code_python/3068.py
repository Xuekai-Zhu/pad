def solution():
    # Calculate the number of non-defective units
    non_defective_units = 20 - 5  # 20 units of phones with 5 defective units
    # Calculate the number of units sold to customers A and C
    units_sold_AC = 3 + 7  # customer A bought 3 units and customer C bought 7 units
    # Calculate the number of units sold to customer B
    units_sold_B = non_defective_units - units_sold_AC
    result = units_sold_B
    return result

print(solution())