def solution():
    """Alfred is storing a tonne of maize each month for the next 2 years. If 5 tonnes are stolen and 8 tonnes are given to him as a donation, how many tonnes of maize does he have at the end of the 2 years."""
    maize_per_month = 1
    months_in_two_years = 24
    total_maize = maize_per_month * months_in_two_years
    maize_stolen = 5
    maize_donated = 8
    final_maize = total_maize - maize_stolen + maize_donated
    result = final_maize
    return result

print(solution())