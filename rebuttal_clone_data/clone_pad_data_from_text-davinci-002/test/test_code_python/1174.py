def solution():
    total_raised = 2500
    percent_donated = 80
    donation_amount = total_raised * (percent_donated / 100)
    num_organizations = 8
    per_organization_donation = donation_amount / num_organizations
    result = per_organization_donation
    return result

print(solution())