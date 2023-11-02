def solution():
    """Alfred is storing a tonne of maize each month for the next 2 years. If 5 tonnes are stolen and 8 tonnes are given to him as a donation, how many tonnes of maize does he have at the end of the 2 years?"""
    maize_per_month = 1
    months_in_2_years = 24
    total_maize = maize_per_month * months_in_2_years
    total_maize -= 5  # subtract stolen maize
    total_maize += 8  # add donated maize
    result = total_maize
    return result

print(solution())