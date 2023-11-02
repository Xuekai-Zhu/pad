def solution():
    
    total_sales = 380
    broccoli_sales = 57
    carrot_sales = 2 * broccoli_sales
    spinach_sales = (carrot_sales / 2) + 16
    cauliflower_sales = total_sales - broccoli_sales - carrot_sales - spinach_sales
    result = cauliflower_sales
    return result

print(solution())