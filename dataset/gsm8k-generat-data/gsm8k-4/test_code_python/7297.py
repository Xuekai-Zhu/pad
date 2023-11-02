def solution():
    """After collecting all the old electronics in their house, Lauryn made $2000 from selling the items on eBay. If her friend Aurelia also made 70% of what she sold on eBay after selling her used electronics, calculate the total amount of money the two friends made on eBay."""
    # Define Lauryn's earnings and Aurelia's earnings as a percentage of Lauryn's
    lauryn_earnings = 2000
    aurelia_earnings_percentage = 0.7

    # Calculate Aurelia's earnings
    aurelia_earnings = lauryn_earnings * aurelia_earnings_percentage

    # Calculate the total earnings of the two friends
    total_earnings = lauryn_earnings + aurelia_earnings

    result = total_earnings
    return result

print(solution())