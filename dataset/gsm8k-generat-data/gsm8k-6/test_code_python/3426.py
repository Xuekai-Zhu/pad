def solution():
    # Calculate the number of bills Lorie will have after making the changes
    bills_100 = 2  # initial number of $100 bills
    bills_50 = 1  # one $100 bill is changed into $50 bills
    remaining_100 = bills_100 - bills_50  # number of remaining $100 bills
    bills_10 = (1/2) * remaining_100  # half of the remaining $100 bill is changed to $10 bills
    bills_5 = remaining_100 - bills_10  # the rest of the remaining $100 bill is changed to $5 bills
    total_bills = bills_50 + remaining_100 + bills_10 + bills_5
    result = total_bills
    return result

print(solution())