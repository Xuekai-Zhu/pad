def solution():
    
    # Define the number of customers and the number of DVDs sold on each customer
    num_customers = 8
    dvd_sold_customers = [1, 2, 2, 3]

    # Calculate the total number of DVDs sold
    total_dvds_sold = sum(dvd_sold_customers)

    # Display the total number of DVDs sold
    result = total_dvds_sold
    return result

print(solution())