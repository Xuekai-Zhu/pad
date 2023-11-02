def solution():
    num_cakes = 10
    slices_per_cake = 8
    slice_price = 1.0
    b1_donation = 0.5  # donation per slice from business 1
    b2_donation = 0.25  # donation per slice from business 2

    # Calculate total number of slices
    total_slices = num_cakes * slices_per_cake

    # Calculate total revenue from selling slices
    total_revenue = total_slices * slice_price

    # Calculate total donations from business 1 and 2
    b1_total_donation = total_slices * b1_donation
    b2_total_donation = total_slices * b2_donation

    # Calculate total amount of money raised
    total_money_raised = total_revenue + b1_total_donation + b2_total_donation
    result = total_money_raised
    return result

print(solution())