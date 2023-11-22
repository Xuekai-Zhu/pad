def solution():
    
    # Define the number of shoes purchased per month and the cost per year
    shoes_per_month = 2
    cost_per_year = 40000

    # Calculate the total cost of shoes purchased per year
    total_cost = shoes_per_month * cost_per_year

    # Calculate the average cost per pair of shoes purchased per year
    avg_cost = total_cost / shoes_per_month

    # Display the average cost per pair of shoes purchased
    result = avg_cost
    return result

print(solution())