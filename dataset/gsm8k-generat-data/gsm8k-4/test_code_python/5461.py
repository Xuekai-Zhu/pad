def solution():
    """June's mom promises to pay her 1 cent for every cloverleaf she picks from the lawn. June picks 200 clovers in total. 75% have 3 petals. 24% have two petals and 1% have four petals. How many cents does June earn?"""
    # Define the number of clovers and the payment per clover
    clovers = 200
    payment_per_clover = 1

    # Calculate the number of clovers with three petals
    clovers_three_petals = clovers * 0.75

    # Calculate the number of clovers with two petals
    clovers_two_petals = clovers * 0.24

    # Calculate the number of clovers with four petals
    clovers_four_petals = clovers * 0.01

    # Calculate the total earnings
    total_earnings = (clovers_three_petals + clovers_two_petals + clovers_four_petals) * payment_per_clover

    # return the result
    result = total_earnings
    return result

print(solution())