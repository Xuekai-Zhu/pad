def solution():
    # Define the initial number of TVs sold
    initial_sales = 327
    # Define the number of years to consider
    years = 3
    # Define the increase in sales each year
    increase_per_year = 50
    
    # Calculate the total increase in sales over the years
    total_increase = increase_per_year * years
    
    # Calculate the final sales number
    final_sales = initial_sales + total_increase
    
    result = final_sales
    return result

print(solution())