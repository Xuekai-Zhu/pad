def solution():
    planned_sales = 500
    thursday_sales = 210
    friday_sales = 2 * thursday_sales
    saturday_sales = 130
    sunday_sales = 0.5 * saturday_sales

    # Calculate the total sales for all days
    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales

    # Calculate how much meat they sold beyond their original plans
    extra_sales = total_sales - planned_sales
    result = extra_sales
    return result

print(solution())