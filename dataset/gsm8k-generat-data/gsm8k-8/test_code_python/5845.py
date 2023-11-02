def solution():
    # Calculate the number of cake slices
    num_slices = 10 * 8

    # Calculate the total amount earned from selling slices
    total_earned = num_slices * 1

    # Calculate the amount earned from the first business owner's donation
    business1_donation = num_slices * 0.5

    # Calculate the amount earned from the second business owner's donation
    business2_donation = num_slices * 0.25

    # Calculate the total amount raised
    total_raised = total_earned + business1_donation + business2_donation
    result = total_raised
    return result

print(solution())