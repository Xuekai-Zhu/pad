def solution():
    """Tim decides to run a campaign for governor. He gets the maximum $1200 donation from 500 people, and three times as many people donated half this sum of money to his campaign. These donations together accounted for 40% of the total money that Tim raised. How much total money did he raise?"""
    # Define the number of people who made the maximum donation and the amount of the donation
    num_max_donors = 500
    max_donation = 1200

    # Calculate the total amount raised from max donors
    max_donors_total = num_max_donors * max_donation

    # Calculate the number of people who made the smaller donation
    num_small_donors = 3 * num_max_donors

    # Calculate the amount of the smaller donation
    small_donation = max_donation / 2

    # Calculate the total amount raised from small donors
    small_donors_total = num_small_donors * small_donation

    # Calculate the total amount raised
    total_raised = (max_donors_total + small_donors_total) / 0.4

    result = total_raised
    return result

print(solution())