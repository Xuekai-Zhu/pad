def solution():
    pencils_per_day = 100  # Paul makes 100 pencils per day
    work_days_per_week = 5  # Paul works 5 days per week
    starting_stock = 80  # Paul starts the week with 80 pencils in stock
    pencils_sold = 350  # Paul sells 350 pencils during the week

    # Calculate the total number of pencils made during the week
    pencils_made = pencils_per_day * work_days_per_week

    # Calculate the total number of pencils in stock at the end of the week
    ending_stock = starting_stock + pencils_made - pencils_sold
    result = ending_stock
    return result

print(solution())