def solution():
    # Calculate the cost of 4 lollipops and 6 packs of chocolate
    cost = (4*2) + (6*(4*2))  # each chocolate pack costs the same as four lollipops

    # Calculate the amount paid by Blake
    amount_paid = 6 * 10

    # Calculate the change Blake will get back
    change = amount_paid - cost
    
    result = change
    return result

print(solution())