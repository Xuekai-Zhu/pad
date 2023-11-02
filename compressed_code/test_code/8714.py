def solution():
    
    starting_sales = 327
    annual_increase = 50
    num_years = 3
    total_increase = annual_increase * num_years
    future_sales = starting_sales + total_increase
    result = future_sales
    return result

print(solution())