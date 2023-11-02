def solution():
    """June's mom promises to pay her 1 cent for every cloverleaf she picks from the lawn. June picks 200 clovers in total. 75% have 3 petals. 24% have two petals and 1% have four petals. How many cents does June earn?"""
    total_clovers = 200
    three_petals = int(total_clovers * 0.75)
    two_petals = int(total_clovers * 0.24)
    four_petals = total_clovers - three_petals - two_petals
    total_earnings = (three_petals + two_petals + four_petals) * 1
    result = total_earnings
    return result

print(solution())