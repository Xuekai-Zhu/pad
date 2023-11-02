def solution():
    """Tim decides to run a campaign for governor. He gets the maximum $1200 donation from 500 people, and three times as many people donated half this sum of money to his campaign. These donations together accounted for 40% of the total money that Tim raised. How much total money did he raise?"""
    max_donation = 1200
    max_donors = 500
    other_donors = 3 * max_donors
    other_donation = 0.5 * max_donation
    total_money_raised = (max_donation * max_donors) + (other_donors * other_donation)
    percent_accounted_for = 40
    total_money_raised_percent = total_money_raised / (percent_accounted_for / 100)
    result = total_money_raised_percent
    return result

print(solution())