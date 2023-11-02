def solution():
    """A restaurant is offering a fundraiser one day where they donate $2 for every $10 donated by customers. The average customer donates 3 and there are 40 customers that day. How much does the restaurant donate?"""
    donation_per_customer = 3
    num_customers = 40
    total_donation = donation_per_customer * num_customers
    donation_ratio = 10 / total_donation
    restaurant_donation = donation_ratio * 2 * total_donation
    result = restaurant_donation
    return result

print(solution())