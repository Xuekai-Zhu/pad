def solution():
    max_donation = 1200
    num_max_donors = 500
    half_max_donation = max_donation / 2
    num_half_donors = num_max_donors * 3

    total_raised_from_max_donors = max_donation * num_max_donors
    total_raised_from_half_donors = half_max_donation * num_half_donors

    total_raised_percent = 0.4
    total_raised = (total_raised_from_max_donors + total_raised_from_half_donors) / total_raised_percent
    result = total_raised
    return result

print(solution())