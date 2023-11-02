def solution():
    """At a CD store, 40% of the CDs cost $10 each, and the rest cost $5 each. Prince bought half the CDs sold at $10 each, and all of the CDs sold at $5 each. If the total number of CDs was 200, how much money did Prince spend on buying the CDs?"""
    # Define the total number of CDs and the percentage of CDs that cost $10
    total_cds = 200
    ten_dollar_percent = 0.4

    # Calculate the number of CDs that cost $10 and $5
    ten_dollar_cds = total_cds * ten_dollar_percent
    five_dollar_cds = total_cds - ten_dollar_cds

    # Calculate the number of CDs that Prince bought at $10 each
    prince_ten_dollar_cds = ten_dollar_cds / 2

    # Calculate the total amount spent by Prince on buying CDs
    total_spent = (prince_ten_dollar_cds * 10) + (five_dollar_cds * 5)

    # Return the result
    result = total_spent
    return result

print(solution())