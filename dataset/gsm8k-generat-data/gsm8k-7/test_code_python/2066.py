def solution():
    donation_per_customer = 3
    num_customers = 40
    donation_threshold = 10
    donation_amount = 2

    # Calculate the total amount donated by customers
    total_donation = donation_per_customer * num_customers

    # Calculate the total amount matching donation by the restaurant
    total_matching_donation = (total_donation // donation_threshold) * donation_amount

    result = total_matching_donation
    return result

print(solution())