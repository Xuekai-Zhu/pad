def solution():
    """Jack has 42 pounds, 11 euros, and 3000 yen. If there are 2 pounds per euro and 100 yen per pound, how much does Jack have in yen?"""
    # Define the given amounts
    pounds = 42
    euros = 11
    yen = 3000

    # Convert euros to pounds
    pounds += euros * 2

    # Convert pounds to yen
    yen += pounds * 100

    # return the result
    result = yen
    return result

print(solution())