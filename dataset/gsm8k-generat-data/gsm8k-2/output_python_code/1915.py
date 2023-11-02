def solution():
    """The Donaldsons pay $15 per hour for babysitting. The Merck family pays $18 per hour and the Hille family pays $20 per hour for babysitting. Layla babysat for the Donaldsons for 7 hours, the Merck family for 6 hours and the Hille family for 3 hours. How many dollars did Layla earn babysitting?"""
    rate_donaldsons = 15
    rate_merck = 18
    rate_hille = 20
    hours_donaldsons = 7
    hours_merck = 6
    hours_hille = 3

    earnings_donaldsons = rate_donaldsons * hours_donaldsons
    earnings_merck = rate_merck * hours_merck
    earnings_hille = rate_hille * hours_hille

    total_earnings = earnings_donaldsons + earnings_merck + earnings_hille

    result = total_earnings
    return result

print(solution())