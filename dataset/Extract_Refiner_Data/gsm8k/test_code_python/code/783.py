def solution():
    
    total_sales = 40
    smart_sales = total_sales / 4
    analog_sales = total_sales / 8
    OLED_sales = total_sales - smart_sales - analog_sales
    result = OLED_sales
    return result

print(solution())