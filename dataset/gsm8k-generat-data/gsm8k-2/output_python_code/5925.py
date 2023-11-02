def solution():
    """Jack has 42 pounds, 11 euros, and 3000 yen. If there are 2 pounds per euro and 100 yen per pound, how much does Jack have in yen?"""
    pound_to_euro_rate = 2
    yen_to_pound_rate = 100
    total_pounds = 42 + (11 * pound_to_euro_rate)
    total_yen = total_pounds * yen_to_pound_rate + 3000
    result = total_yen
    return result

print(solution())