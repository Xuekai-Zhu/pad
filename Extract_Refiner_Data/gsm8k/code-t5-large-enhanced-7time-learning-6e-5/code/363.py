def solution():
    
    # Define the number of customers who were kicked out for refusing to wear masks
    refusing_customers = 3

    # Calculate the number of customers who were kicked out for shoplifting
    shoplifting_customers = 4 * refusing_customers - 5

    # Calculate the number of shoplifters who were kicked out for physical violence over goods on sale
    physical_violations_customers = 3 * shoplifting_customers

    # Calculate the total number of people who were kicked out for other reasons
    other_customers = 50 - refusing_customers - shoplifting_customers - physical_violations_customers

    # Display the number of customers who were kicked out for other reasons
    result = other_customers
    return result

print(solution())