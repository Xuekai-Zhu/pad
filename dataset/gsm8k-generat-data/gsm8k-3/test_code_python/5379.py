def solution():
    """Gina is considered a bad tipper because she tipped 5%. If good tippers tip at least 20%, how many more cents than normal would Gina have to tip on a bill of $26 to be considered a good tipper?"""
    # Define the bill amount and tip percentages
    bill = 26
    bad_tip_percentage = 0.05
    good_tip_percentage = 0.20

    # Calculate the amount of a good tip
    good_tip_amount = bill * good_tip_percentage

    # Calculate the amount of a bad tip
    bad_tip_amount = bill * bad_tip_percentage

    # Calculate the difference between a good and bad tip
    difference = good_tip_amount - bad_tip_amount

    # Convert the difference to cents
    difference_cents = difference * 100

    # Display the difference in cents
    result = difference_cents
    return result

print(solution())