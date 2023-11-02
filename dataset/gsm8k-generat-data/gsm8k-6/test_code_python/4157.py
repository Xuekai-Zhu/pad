def solution():
    # Calculate the total number of biscuits needed
    total_biscuits = 18 * 2  # Lady Bird wants to make 2 biscuits per guest for 18 guests

    # Calculate the amount of flour needed for total biscuits
    flour_per_biscuit = 5/4  # Lady Bird uses 1 1/4 cup flour to make 9 biscuits
    flour_needed = (total_biscuits/9) * flour_per_biscuit 

    result = flour_needed
    return result

print(solution())