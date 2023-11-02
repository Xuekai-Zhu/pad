def solution():
    houses_visited = 20
    sales_on_first_day = houses_visited
    sales_on_second_day = houses_visited * 2 * 0.8
    total_sales = sales_on_first_day + sales_on_second_day
    items_sold = total_sales * 2
    result = items_sold
    return result

print(solution())