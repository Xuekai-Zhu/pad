def solution():
    initial_stock = # the number of bicycles Hank had at the start
    friday_sales = 10
    friday_restock = 15
    saturday_sales = 12
    saturday_restock = 8
    sunday_sales = 9
    sunday_restock = 11
    
    # Calculate the net change in stock from Friday to Sunday
    net_change = (friday_restock + saturday_restock + sunday_restock) - (friday_sales + saturday_sales + sunday_sales)
    
    # Calculate the final stock
    final_stock = initial_stock + net_change
    result = net_change
    return result

print(solution())