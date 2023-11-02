def solution():
    # Calculate the total number of slices
    total_slices = 10 * 8  # 10 cakes with 8 slices per cake

    # Calculate the total amount raised by selling slices
    total_sales = total_slices * 1  # each slice sells for $1

    # Calculate the total amount raised by the first business owner's donation
    donation_1 = total_slices * 0.5  # the first business owner donates 50 cents per slice

    # Calculate the total amount raised by the second business owner's donation
    donation_2 = total_slices * 0.25  # the second business owner donates 25 cents per slice

    # Calculate the total amount raised
    total_raised = total_sales + donation_1 + donation_2
    result = total_raised
    return result

print(solution())