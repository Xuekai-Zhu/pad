def solution():
    # Calculate the total cost of the parking tickets
    ticket1 = 150
    ticket2 = 150
    ticket3 = ticket1 / 3
    total_cost = ticket1 + ticket2 + ticket3
    
    # Calculate the amount James' roommate pays
    roommate_payment = total_cost / 2
    
    # Calculate the amount James has left in the bank
    starting_amount = 500
    remaining_amount = starting_amount - (total_cost - roommate_payment)
    
    result = remaining_amount
    return result

print(solution())