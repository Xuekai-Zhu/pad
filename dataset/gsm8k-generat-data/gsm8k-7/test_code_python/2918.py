def solution():
    num_guests = 20
    regular_price = 25.0
    discount = 0.1 # 10% discount for repeat customers

    # Calculate the total revenue if all guests pay the regular price
    total_regular_revenue = num_guests * regular_price

    # Calculate the revenue from Phoebe's party with the discount
    phoebe_discounted_price = regular_price * (1 - discount)
    phoebe_revenue = phoebe_discounted_price * num_guests

    # Calculate Monica's total revenue from all parties, including Phoebe's
    total_revenue = total_regular_revenue + phoebe_revenue
    result = total_revenue
    return result

print(solution())