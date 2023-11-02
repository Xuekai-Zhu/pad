def solution():
    max_donation = 1200  # Tim gets a maximum donation of $1200 from 500 people
    num_max_donors = 500  # 500 people donate the maximum amount

    # Calculate the total amount donated by people who donated less than the maximum amount
    smaller_donation = max_donation / 2  # People donated half of the maximum amount
    num_smaller_donors = num_max_donors * 3  # Three times as many people donated smaller amounts
    total_smaller_donation = smaller_donation * num_smaller_donors

    # Calculate the total amount donated
    total_donation = (max_donation * num_max_donors) + total_smaller_donation

    # Calculate the total amount raised
    total_money_raised = total_donation / 0.4  # Donations accounted for 40% of the total money raised
    result = total_money_raised
    return result

print(solution())