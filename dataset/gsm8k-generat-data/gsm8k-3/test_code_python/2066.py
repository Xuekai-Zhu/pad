def solution():
    """A restaurant is offering a fundraiser one day where they donate $2 for every $10 donated by customers. The average customer donates 3 and there are 40 customers that day. How much does the restaurant donate?"""
    # Define the donation per customer and the number of customers
    DONATION_PER_CUSTOMER = 2
    AVERAGE_DONATION = 3
    NUM_CUSTOMERS = 40

    # Calculate the total amount donated by customers
    total_donation = AVERAGE_DONATION * NUM_CUSTOMERS

    # Calculate the amount donated by the restaurant
    restaurant_donation = (total_donation // 10) * DONATION_PER_CUSTOMER

    # Display the amount donated by the restaurant
    result = restaurant_donation
    return result

print(solution())