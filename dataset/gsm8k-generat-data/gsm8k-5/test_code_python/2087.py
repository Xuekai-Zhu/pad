def solution():
    amount_donated = 0.8 * 2500  # 80% of the raised amount is donated
    num_organizations = 8  # There are 8 organizations receiving the donation

    # Calculate the amount of money each organization will receive
    amount_per_organization = amount_donated / num_organizations
    result = amount_per_organization
    return result

print(solution())