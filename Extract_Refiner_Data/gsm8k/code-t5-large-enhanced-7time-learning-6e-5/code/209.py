def solution():
    
    # Define the number of customers counted on the first day
    day1_customers = 100

    # Calculate the number of customers counted on the second day
    day2_customers = day1_customers + 50

    # Calculate the total number of customers counted on the third day
    total_customers = 500
    day3_customers = total_customers - day1_customers - day2_customers

    # Display the number of customers counted on the third day
    result = day3_customers
    return result

print(solution())