def solution():
    """June's mom promises to pay her 1 cent for every cloverleaf she picks from the lawn. June picks 200 clovers in total. 75% have 3 petals. 24% have two petals and 1% have four petals. How many cents does June earn?"""
    total_clovers = 200
    three_petals = 0.75 * total_clovers
    two_petals = 0.24 * total_clovers
    four_petals = 0.01 * total_clovers
    cents_earned = int((three_petals * 1) + (two_petals * 1) + (four_petals * 1))
    result = cents_earned
    return result

print(solution())