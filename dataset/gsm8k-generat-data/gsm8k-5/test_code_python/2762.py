def solution():
    bottles_per_month = 15  # Henry drinks 15 bottles of kombucha every month
    cost_per_bottle = 3.00  # Each bottle costs $3.00
    refund_per_bottle = 0.10  # He gets a $0.10 cash refund for each bottle when he recycles it
    months_per_year = 12  # There are 12 months in a year

    # Calculate the total cost of the kombucha he drinks in a year
    total_cost = bottles_per_month * cost_per_bottle * months_per_year

    # Calculate the total refund he will receive for recycling the bottles
    total_refund = bottles_per_month * refund_per_bottle * months_per_year

    # Calculate the number of bottles he can buy with the refund
    bottles_bought = total_refund / cost_per_bottle
    result = bottles_bought
    return result

print(solution())