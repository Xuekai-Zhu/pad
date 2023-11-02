def solution():
    # Define the variables
    max_donation = 1200
    num_max_donors = 500
    half_max_donation = max_donation / 2
    num_half_donors = 3 * num_max_donors
    total_donors = num_max_donors + num_half_donors
    total_donated = (max_donation * num_max_donors) + (half_max_donation * num_half_donors)
    total_percent = 40

    # Calculate the total amount raised
    total_raised = (total_donated / total_percent) * 100

    result = total_raised
    return result

print(solution())