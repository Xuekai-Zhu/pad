def solution():
    guests = 6  # Antoine is inviting 6 people over
    meat_per_person = 0.5  # Antoine needs 1/2 pound of meat per person
    beef_tenderloin_price = 15.00  # The price of beef tenderloin is $15.00 per pound

    # Calculate the total amount of meat needed
    total_meat = guests * meat_per_person

    # Calculate the cost of the meat
    meat_cost = total_meat * beef_tenderloin_price
    result = meat_cost
    return result

print(solution())