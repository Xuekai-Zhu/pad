def solution():
    bill = 26  # The bill is $26
    bad_tip_percentage = 0.05  # Gina is considered a bad tipper because she tips 5%
    good_tip_percentage = 0.2  # Good tippers tip at least 20%

    # Calculate the amount of tip Gina would leave if she tipped 20%
    good_tip = bill * good_tip_percentage

    # Calculate how much more Gina would have to tip to be considered a good tipper
    difference = good_tip - (bill * bad_tip_percentage)

    # Convert the difference to cents
    difference_cents = difference * 100
    result = int(difference_cents)
    return result

print(solution())