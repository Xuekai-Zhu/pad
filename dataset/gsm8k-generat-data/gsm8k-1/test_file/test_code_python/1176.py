def solution():
    """A company sold 4000 gallons of milk in jars to Mr. Marcellus' store at the cost of $3.5 per gallon. However, Mr. Marcellus later realized 2/5 of the amount of milk he purchased had passed the expiry date and could not be sold. He returned the sour milk to the company and ordered a refund. Calculate how much he got in refunds."""
    total_gallons = 4000
    cost_per_gallon = 3.5
    expired_gallons = total_gallons * 2/5
    usable_gallons = total_gallons - expired_gallons
    refund = expired_gallons * cost_per_gallon
    result = refund
    return result

print(solution())