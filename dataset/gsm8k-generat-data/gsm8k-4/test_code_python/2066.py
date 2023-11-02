def solution():
    """A restaurant is offering a fundraiser one day where they donate $2 for every $10 donated by customers. The average customer donates 3 and there are 40 customers that day. How much does the restaurant donate?"""
    # Define the donation amount per customer
    donation_per_customer = 2

    # Define the donation threshold for the restaurant
    donation_threshold = 10

    # Calculate the total amount donated by customers
    total_donation_amount = 40 * 3
    
    # Calculate the number of times the donation threshold was met
    donations_met_threshold = total_donation_amount // donation_threshold

    # Calculate the total donation amount from the restaurant
    total_donation = donations_met_threshold * donation_per_customer

    # Return the result
    result = total_donation
    return result

print(solution())