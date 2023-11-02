def solution():
    sales_on_monday = 2
    sales_on_tuesday = sales_on_monday + 1
    sales_on_wednesday = sales_on_tuesday + 1
    sales_on_thursday = sales_on_wednesday + 1
    sales_on_friday = sales_on_thursday + 1
    sales_on_saturday = sales_on_friday + 1
    sales_on_sunday = sales_on_saturday + 1
    total_sales = sales_on_monday + sales_on_tuesday + sales_on_wednesday + sales_on_thursday + sales_on_friday + sales_on_saturday + sales_on_sunday
    average_sales = total_sales / 7
    result = average_sales
    return result

print(solution())