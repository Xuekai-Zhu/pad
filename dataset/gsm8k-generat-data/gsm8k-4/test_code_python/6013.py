def solution():
    """Melisa and Jennifer threw a fiftieth birthday party for their father at a local restaurant. When the bill came, Melisa added a 15% tip of $42. Jennifer said that the service was wonderful and they should leave a 20% tip instead. How much is a 20% tip?"""
    # Calculate the total bill
    total_bill = 100

    # Calculate the amount of the 15% tip
    tip_15_percent = 42

    # Calculate the bill without the 15% tip
    bill_without_tip = total_bill - tip_15_percent

    # Calculate the 20% tip amount
    tip_20_percent = bill_without_tip * 0.2

    # return the result
    result = tip_20_percent
    return result

print(solution())