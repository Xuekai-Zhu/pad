def solution():
    """A restaurant is offering a fundraiser one day where they donate $2 for every $10 donated by customers. The average customer donates 3 and there are 40 customers that day. How much does the restaurant donate?"""
    donation_per_customer = 3
    total_customers = 40
    donation_ratio = 10 / donation_per_customer
    total_donation = donation_ratio * total_customers
    restaurant_donation = 2 * total_donation
    result = restaurant_donation
    return result

print(solution())