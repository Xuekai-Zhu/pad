def solution():
    # Define the donation amount per customer
    donation_per_customer = 2/10 * 10

    # Calculate the total donation by all customers
    total_donation = donation_per_customer * 3 * 40

    # Calculate the amount donated by the restaurant
    restaurant_donation = 2/10 * total_donation

    result = restaurant_donation
    return result

print(solution())