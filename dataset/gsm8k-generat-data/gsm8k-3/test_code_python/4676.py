def solution():
    """Tim decides to run a campaign for governor.  He gets the maximum $1200 donation from 500 people, and three times as many people donated half this sum of money to his campaign.  These donations together accounted for 40% of the total money that Tim raised.  How much total money did he raise?"""
    # Define the maximum donation and the number of people who donated this amount
    MAX_DONATION = 1200
    MAX_DONORS = 500

    # Calculate the total amount raised from the maximum donors
    max_donation_total = MAX_DONATION * MAX_DONORS

    # Calculate the reduced donation amount and the number of donors
    reduced_donation = MAX_DONATION / 2
    reduced_donors = MAX_DONORS * 3

    # Calculate the total amount raised from the reduced donors
    reduced_donation_total = reduced_donation * reduced_donors

    # Calculate the total amount raised in the campaign
    total_raised = (max_donation_total + reduced_donation_total) / 0.4

    # Display the total amount raised
    result = total_raised
    return result

print(solution())