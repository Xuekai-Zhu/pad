def solution():
    
    # Define the total cost of groceries and the cost of Madeline
    total_cost = 400
    madeline_cost = total_cost * 0.6

    # Calculate Keenan's total cost per month
    keenan_cost = total_cost - madeline_cost

    # Calculate Keenan's cost per week
    keenan_weekly_cost = keenan_cost * 4

    # Display Keenan's weekly cost
    result = keenan_weekly_cost
    return result

print(solution())