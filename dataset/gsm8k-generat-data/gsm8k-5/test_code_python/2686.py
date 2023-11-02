def solution():
    # Let's assume the weight of the fish Peter caught is x kg
    x = 0
    ali = 2 * x  # Ali's catch is twice as much as Peter's
    joey = x + 1  # Joey's catch is 1 kg more than Peter's
    total = ali + x + joey  # Total weight of fish caught by all three

    # We know the sum of all three is 25 kg, so we can set up an equation
    # to solve for x, the weight of the fish Peter caught
    x = (25 - 2 - 1) / 4  # 2 kg for Ali and 1 kg for Joey

    ali = 2 * x  # Ali's catch is twice as much as Peter's
    result = ali
    return result

print(solution())