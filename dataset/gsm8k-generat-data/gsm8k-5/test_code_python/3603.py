def solution():
    robi_contribution = 4000  # Robi contributed $4000
    rudy_contribution = robi_contribution * 1.25  # Rudy contributed 1/4 more than Robi

    # Calculate the total amount of money contributed
    total_contribution = robi_contribution + rudy_contribution

    # Calculate the profit earned
    profit = total_contribution * 0.2

    # Calculate the amount of money each person gets
    robi_share = (robi_contribution + (profit / 2)) / 2
    rudy_share = (rudy_contribution + (profit / 2)) / 2
    result = (robi_share, rudy_share)
    return result

print(solution())