def solution():
    # Parker's share is 2 parts out of 5 parts in total
    # Let x be the total amount shared, so Parker's share is (2/5) * x
    # We know Parker's share is $50, so we can solve for x
    x = 50 / (2/5)

    # The total amount shared is 5 parts out of 5 parts in total, so
    # Richie's share is (3/5) * x
    total_share = x * 5/2

    result = total_share
    return result

print(solution())