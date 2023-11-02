def solution():
    pounds = 42
    euros = 11
    yen = 3000

    # Convert euros to pounds and add with original pounds
    pounds += euros * 2

    # Convert all pounds to yen and add with original yen
    yen += pounds * 100

    result = yen
    return result

print(solution())