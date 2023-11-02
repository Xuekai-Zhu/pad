def solution():
    
    starting_stock = 800
    monday_sales = 60
    tuesday_sales = 10
    wednesday_sales = 20
    thursday_sales = 44
    friday_sales = 66
    total_sold = monday_sales + tuesday_sales + wednesday_sales + thursday_sales + friday_sales
    remaining_stock = starting_stock - total_sold
    result = remaining_stock
    return result

print(solution())