def solution():
    # Calculate the amount of money deducted from the cost of the harvest
    entrance_charge = 4 * 3  # Miguel charged $4 from each of the three pickers
    deducted_amount = 128 - entrance_charge

    # Calculate the number of pounds of strawberries picked by Sally, Jenny, and Moses
    weight = deducted_amount / 20  # $20 per pound of strawberries
    result = weight
    return result

print(solution())