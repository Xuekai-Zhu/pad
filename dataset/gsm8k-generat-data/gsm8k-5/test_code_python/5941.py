def solution():
    # Calculate the total amount of milk Aunt May had
    starting_amount = 15 # gallons left over from yesterday
    morning_amount = 365 # gallons this morning
    evening_amount = 380 # gallons this evening
    total_amount = starting_amount + morning_amount + evening_amount

    # Calculate the amount of milk Aunt May has left after selling to the ice cream factory
    amount_sold = 612 # gallons sold to the ice cream factory
    amount_left = total_amount - amount_sold
    result = amount_left
    return result

print(solution())