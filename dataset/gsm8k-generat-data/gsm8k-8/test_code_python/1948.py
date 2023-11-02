def solution():
    # Define the cost of each size of lemonade
    small_cup = 1
    medium_cup = 2
    large_cup = 3
    
    # Define the total revenue and revenue from small and medium cups
    total_revenue = 50
    small_revenue = 11
    medium_revenue = 24
    
    # Calculate the revenue from large cups
    large_revenue = total_revenue - small_revenue - medium_revenue
    
    # Calculate the number of large cups sold by dividing revenue from large cups by the cost per cup
    num_large_cups = large_revenue // large_cup
    
    result = num_large_cups
    return result

print(solution())