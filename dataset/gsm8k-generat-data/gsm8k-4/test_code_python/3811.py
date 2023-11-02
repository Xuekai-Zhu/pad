def solution():
    """Carmen is selling girl scout cookies. She sells three boxes of samoas to the green house for $4 each; two boxes of thin mints for $3.50 each and one box of fudge delights for $5 to the yellow house; and nine boxes of sugar cookies for $2 each to the brown house. How much money did Carmen make?"""
    # Define the quantities and prices of each type of cookie sold
    samoas_quantity = 3
    samoas_price = 4
    thin_mints_quantity = 2
    thin_mints_price = 3.5
    fudge_quantity = 1
    fudge_price = 5
    sugar_quantity = 9
    sugar_price = 2

    # Calculate the total revenue from selling the cookies
    samoas_revenue = samoas_quantity * samoas_price
    thin_mints_revenue = thin_mints_quantity * thin_mints_price
    fudge_revenue = fudge_quantity * fudge_price
    sugar_revenue = sugar_quantity * sugar_price
    total_revenue = samoas_revenue + thin_mints_revenue + fudge_revenue + sugar_revenue

    # return the result
    result = total_revenue
    return result

print(solution())