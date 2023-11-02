def solution():
    
    hardshell_price = 5
    softshell_price = 2
    family_order = (4 * hardshell_price) + (3 * softshell_price)
    rest_order = 10 * 2 * softshell_price
    total_sales = family_order + rest_order
    result = total_sales
    return result

print(solution())