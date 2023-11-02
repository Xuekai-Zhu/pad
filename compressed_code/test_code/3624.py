def solution():
    
    max_donation = 1200
    num_max_donors = 500
    half_max_donation = max_donation / 2
    num_half_donors = 3 * num_max_donors
    total_donation_amount = (max_donation * num_max_donors) + (half_max_donation * num_half_donors)
    total_money_raised = total_donation_amount / 0.4
    result = total_money_raised
    return result

print(solution())