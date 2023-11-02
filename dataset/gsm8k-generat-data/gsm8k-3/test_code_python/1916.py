def solution():
    """The Donaldsons pay $15 per hour for babysitting. The Merck family pays $18 per hour and the Hille family pays $20 per hour for babysitting. Layla babysat for the Donaldsons for 7 hours, the Merck family for 6 hours and the Hille family for 3 hours. How many dollars did Layla earn babysitting?"""
    # Define the hourly rates for each family
    DONALDSONS_RATE = 15
    MERCK_RATE = 18
    HILLE_RATE = 20

    # Define the number of hours Layla babysat for each family
    donaldsons_hours = 7
    merck_hours = 6
    hille_hours = 3

    # Calculate how much Layla earned from each family
    donaldsons_earnings = donaldsons_hours * DONALDSONS_RATE
    merck_earnings = merck_hours * MERCK_RATE
    hille_earnings = hille_hours * HILLE_RATE

    # Calculate the total amount Layla earned
    total_earnings = donaldsons_earnings + merck_earnings + hille_earnings

    # Display Layla's total earnings
    result = total_earnings
    return result

print(solution())