def solution():
    # Let's assume the number of rock CDs to be "r"
    # Then the number of country CDs would be "r + 3"
    # And the number of classical CDs would be (1/2) * r

    # We know that Henry has 23 country CDs, so we can solve for "r"
    r = 23 - 3  # Since r + 3 = number of country CDs
    classical_cds = int((1/2) * r)  # The number of classical CDs is half of r

    result = classical_cds
    return result

print(solution())