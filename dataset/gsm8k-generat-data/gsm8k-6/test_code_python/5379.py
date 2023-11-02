def solution():
    # Calculate the amount of tip that a good tipper would leave on a $26 bill
    good_tip = 0.20 * 26

    # Calculate the amount of tip that Gina left on the same bill
    gina_tip = 0.05 * 26

    # Calculate the difference between the two tip amounts in cents
    difference = (good_tip - gina_tip) * 100

    result = difference
    return result

print(solution())