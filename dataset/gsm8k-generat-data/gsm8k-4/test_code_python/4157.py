def solution():
    """Lady Bird uses 1 1/4 cup flour to make 9 biscuits. She’s hosting this month's Junior League club which has 18 members and wants to make sure she allows 2 biscuits per guest. How many cups of flour will Lady Bird need?"""
    # Define the amount of flour needed per biscuit
    flour_per_biscuit = 1.25 / 9

    # Calculate the total number of biscuits needed
    biscuits_needed = 18 * 2

    # Calculate the total amount of flour needed
    flour_needed = flour_per_biscuit * biscuits_needed

    # Return the result
    result = round(flour_needed, 2)
    return result

print(solution())