def solution():
    pencils_per_day = 100
    days_per_week = 5
    starting_stock = 80
    pencils_sold = 350

    # Calculate the total number of pencils produced during the week
    total_pencils_produced = pencils_per_day * days_per_week

    # Calculate the total number of pencils in stock at the end of the week
    ending_stock = (starting_stock + total_pencils_produced) - pencils_sold
    result = ending_stock
    return result

print(solution())