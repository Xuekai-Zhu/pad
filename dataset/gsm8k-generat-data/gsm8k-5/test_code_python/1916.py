def solution():
    rate_donaldsons = 15  # The Donaldsons pay $15 per hour
    rate_merck = 18  # The Merck family pays $18 per hour
    rate_hille = 20  # The Hille family pays $20 per hour

    # Calculate the total amount Layla earned babysitting for each family
    earnings_donaldsons = rate_donaldsons * 7  # Layla earned $15 per hour babysitting for 7 hours with the Donaldsons
    earnings_merck = rate_merck * 6  # Layla earned $18 per hour babysitting for 6 hours with the Merck family
    earnings_hille = rate_hille * 3  # Layla earned $20 per hour babysitting for 3 hours with the Hille family

    # Calculate the total amount Layla earned babysitting
    total_earnings = earnings_donaldsons + earnings_merck + earnings_hille
    result = total_earnings
    return result

print(solution())