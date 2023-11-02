def solution():
    num_cakes = 10  # Didi received 10 cakes
    slices_per_cake = 8  # Each cake can be sliced into 8 slices
    price_per_slice = 1  # Didi sold each slice for $1

    # Calculate the total number of slices
    total_slices = num_cakes * slices_per_cake

    # Calculate the total amount raised from selling slices
    money_from_slices = total_slices * price_per_slice

    # Calculate the amount donated from the first business owner
    donation_1 = total_slices * 0.5

    # Calculate the amount donated from the second business owner
    donation_2 = total_slices * 0.25

    # Calculate the total amount raised
    total_money_raised = money_from_slices + donation_1 + donation_2
    result = total_money_raised
    return result

print(solution())