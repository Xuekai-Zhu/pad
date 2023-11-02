def solution():
    flour_per_biscuit = 1.25 / 9  # cups
    num_guests = 18
    biscuits_per_guest = 2

    # Calculate the total number of biscuits needed
    total_biscuits = num_guests * biscuits_per_guest

    # Calculate the total amount of flour needed
    total_flour = total_biscuits * flour_per_biscuit
    result = total_flour
    return result

print(solution())