def solution():
    donation_per_customer = 3  # The average customer donates $3
    total_customers = 40  # There are 40 customers that day
    total_donations = donation_per_customer * total_customers  # Total amount donated by customers

    # Calculate the amount donated by the restaurant
    restaurant_donation = 2 * (total_donations // 10)
    result = restaurant_donation
    return result

print(solution())