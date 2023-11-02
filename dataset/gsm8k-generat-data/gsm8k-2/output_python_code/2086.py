def solution():
    """A private company raised $2500 to be used for charity. They donated 80% to a public foundation with 8 organizations. How much money will each organization receive?"""
    total_donation = 2500 * 0.8
    num_organizations = 8
    donation_per_organization = total_donation / num_organizations
    result = donation_per_organization
    return result

print(solution())