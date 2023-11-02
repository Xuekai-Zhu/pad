def solution():
    rent_per_month = 1250  # Rent for the apartment per month
    deposit = 500  # Deposit required by the landlord
    months_rent_advance = 2  # Number of months' rent required in advance

    total_rent_advance = months_rent_advance * rent_per_month  # Total rent required in advance
    total_cost = total_rent_advance + deposit  # Total cost of renting the apartment

    savings = 2225  # Amount of money Janet has saved
    additional_money_required = total_cost - savings  # Additional money required to rent the apartment

    result = additional_money_required
    return result

print(solution())