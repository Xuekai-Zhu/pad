def solution():
    total_money_donated = 2500  # total money raised by the private company
    foundation_donation = 0.8 * total_money_donated  # 80% of the money donated to the public foundation
    num_organizations = 8  # number of organizations in the public foundation

    # Calculate the amount of money each organization will receive
    money_per_organization = foundation_donation / num_organizations
    result = money_per_organization
    return result

print(solution())