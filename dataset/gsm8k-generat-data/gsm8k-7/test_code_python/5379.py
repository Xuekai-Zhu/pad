def solution():
    bill = 26
    bad_tip = 0.05
    good_tip = 0.2

    # Calculate the amount Gina would tip for a bad tip
    bad_tip_amount = bill * bad_tip

    # Calculate the minimum amount Gina would need to tip for a good tip
    good_tip_amount = bill * good_tip

    # Calculate how many more cents Gina would need to tip for a good tip
    difference = (good_tip_amount - bad_tip_amount) * 100
    result = difference
    return result

print(solution())