def solution():
    rate_donaldsons = 15
    rate_merck = 18
    rate_hille = 20
    hours_donaldsons = 7
    hours_merck = 6
    hours_hille = 3

    # Calculate the total earnings for babysitting each family
    earnings_donaldsons = rate_donaldsons * hours_donaldsons
    earnings_merck = rate_merck * hours_merck
    earnings_hille = rate_hille * hours_hille

    # Calculate the total earnings for all babysitting jobs
    total_earnings = earnings_donaldsons + earnings_merck + earnings_hille
    result = total_earnings
    return result

print(solution())