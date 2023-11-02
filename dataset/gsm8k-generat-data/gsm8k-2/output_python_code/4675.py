def solution():
    """Tim decides to run a campaign for governor. He gets the maximum $1200 donation from 500 people, and three times as many people donated half this sum of money to his campaign. These donations together accounted for 40% of the total money that Tim raised. How much total money did he raise?"""
    max_donation = 1200
    num_max_donors = 500
    half_max_donation = max_donation / 2
    num_half_donors = 3 * num_max_donors
    total_donation_amount = (max_donation * num_max_donors) + (half_max_donation * num_half_donors)
    total_money_raised = total_donation_amount / 0.4
    result = total_money_raised
    return result

print(solution())