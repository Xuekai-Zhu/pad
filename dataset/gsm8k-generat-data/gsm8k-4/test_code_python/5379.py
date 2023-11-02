def solution():
    """Gina is considered a bad tipper because she tipped 5%. If good tippers tip at least 20%, how many more cents than normal would Gina have to tip on a bill of $26 to be considered a good tipper?"""
    # Define the bill amount
    bill = 26

    # Calculate the normal amount Gina would tip (5%)
    normal_tip = bill * 0.05

    # Calculate the amount she would have to tip to reach 20%
    good_tip = bill * 0.2

    # Calculate the difference
    difference = good_tip - normal_tip

    # Convert the difference to cents
    difference_cents = difference * 100

    # Return the result
    result = difference_cents
    return result

print(solution())