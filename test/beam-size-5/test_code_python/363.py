def solution():
    
    # Define the number of customers kicked out for refusing
    refusing_customers = 3

    # Calculate the number of customers kicked out for shoplifting
    shoplifting_customers = (4 * refusing_customers) - 5

    # Calculate the number of customers kicked out for physical violence over goods
    violence_customers = 3 * shoplifting_customers

    # Calculate the number of customers kicked out for other reasons
    other_customers = 50 - (shoplifting_customers + violence_customers)

    # Display the number of customers kicked out for other reasons
    result = other_customers
    return result

print(solution())