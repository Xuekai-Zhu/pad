def solution():
    cake_donations = 10
    slices_per_cake = 8
    slice_price = 1
    donation_1 = 0.5
    donation_2 = 0.25
    total_slices = cake_donations * slices_per_cake
    total_revenue = total_slices * slice_price
    total_donations = (total_slices * donation_1) + (total_slices * donation_2)
    total_raised = total_revenue + total_donations
    result = total_raised
    return result

print(solution())