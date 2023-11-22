def solution():
    
    # Define the cost of each phone and the number of phones purchased
    PHONE_COST = 700
    NUM_PHONES = 5

    # Calculate the total cost of the phones
    total_cost = PHONE_COST * NUM_PHONES

    # Calculate the amount paid by the seller
    amount_paid = 4000

    # Calculate the change
    change = amount_paid - total_cost

    # Display the change
    result = change
    return result

print(solution())