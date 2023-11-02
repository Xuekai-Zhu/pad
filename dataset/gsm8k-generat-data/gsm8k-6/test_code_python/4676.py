def solution():
    # Calculate the total amount of money raised by Tim
    max_donation = 1200  # maximum donation per person
    num_max_donors = 500  # number of people who donated the maximum amount
    total_max_donations = max_donation * num_max_donors  # total amount donated by these people
    num_half_donors = 3 * num_max_donors  # three times as many people donated half the maximum amount
    half_donation = max_donation / 2  # half the maximum donation amount
    total_half_donations = half_donation * num_half_donors  # total amount donated by these people
    percent_total = 40  # the sum of these donations accounted for 40% of the total funds raised
    total_raised = (total_max_donations + total_half_donations) * 100 / percent_total  # total amount raised
    result = total_raised
    return result

print(solution())