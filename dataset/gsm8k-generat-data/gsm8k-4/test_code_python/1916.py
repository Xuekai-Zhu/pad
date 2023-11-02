def solution():
    """The Donaldsons pay $15 per hour for babysitting. The Merck family pays $18 per hour and the Hille family pays $20 per hour for babysitting. Layla babysat for the Donaldsons for 7 hours, the Merck family for 6 hours and the Hille family for 3 hours. How many dollars did Layla earn babysitting?"""
    # Define the hourly rates for each family
    rate_donaldsons = 15
    rate_merck = 18
    rate_hille = 20
    
    # Define the number of hours worked for each family
    hours_donaldsons = 7
    hours_merck = 6
    hours_hille = 3
    
    # Calculate the total amount earned by babysitting
    earnings = (rate_donaldsons * hours_donaldsons) + (rate_merck * hours_merck) + (rate_hille * hours_hille)

    result = earnings
    return result

print(solution())