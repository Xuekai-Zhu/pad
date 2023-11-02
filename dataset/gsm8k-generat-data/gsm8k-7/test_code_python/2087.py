def solution():
    total_fund_raised = 2500
    donation_percentage = 0.8  # 80% donation
    num_organizations = 8

    # Calculate the total amount of money donated to the public foundation
    donation_amount = total_fund_raised * donation_percentage

    # Calculate the amount of money each organization will receive
    organization_share = donation_amount / num_organizations
    result = organization_share
    return result

print(solution())