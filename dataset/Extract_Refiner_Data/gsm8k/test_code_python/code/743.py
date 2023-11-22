def solution():
    
    # Define the number of tomatoes sold per day and the cost per tomato
    TOMATOES_PER_DAY = 500
    COST_PER_TOMATO = 0.5

    # Calculate the total cost per day
    total_cost_per_day = TOMATOES_PER_DAY * COST_PER_TOMATO

    # Calculate the total revenue per day
    total_revenue_per_day = TOMATOES_PER_DAY * 0.4

    # Calculate the savings per day
    savings_per_day = total_revenue_per_day - total_cost_per_day

    # Calculate the savings per week
    savings_per_week = savings_per_day * 7

    # Display the savings per week
    result = savings_per_week
    return result

print(solution())