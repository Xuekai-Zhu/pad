def solution():
    
    # Define the number of customers Jewel processes
    jewel_customers = 50

    # Calculate the number of customers Julie operates the cash register
    julie_customers = jewel_customers * 2

    # Calculate the total weekly production for the two
    total_production = (jewel_customers + julie_customers) * 7

    # Display the total weekly production
    result = total_production
    return result

print(solution())