def solution():
    
    num_cakes = 10
    slices_per_cake = 8
    slice_price = 1
    slice_donation_1 = 0.5
    slice_donation_2 = 0.25
    total_slices = num_cakes * slices_per_cake
    total_sales = total_slices * slice_price
    total_donation_1 = total_slices * slice_donation_1
    total_donation_2 = total_slices * slice_donation_2
    total_funds_raised = total_sales + total_donation_1 + total_donation_2
    result = total_funds_raised
    return result

print(solution())