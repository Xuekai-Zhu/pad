def solution():
    maize_per_month = 1  # Alfred is storing 1 tonne of maize each month
    total_months = 2 * 12  # Alfred is storing maize for the next 2 years, which is 24 months

    # Calculate the total amount of maize stored over 2 years
    total_maize = maize_per_month * total_months

    # Subtract the stolen maize and add the donated maize
    net_maize = total_maize - 5 + 8

    result = net_maize
    return result

print(solution())