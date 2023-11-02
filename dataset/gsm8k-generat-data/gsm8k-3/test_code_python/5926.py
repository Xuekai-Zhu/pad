def solution():
    """Jack has 42 pounds, 11 euros, and 3000 yen. If there are 2 pounds per euro and 100 yen per pound, how much does Jack have in yen?"""
    # Convert euros to pounds
    euro_to_pounds = 2
    pounds = 42 + 11 * euro_to_pounds

    # Convert pounds to yen
    yen_to_pounds = 100
    yen = pounds * yen_to_pounds + 3000

    # Display the amount in yen
    result = yen
    return result

print(solution())