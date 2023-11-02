def solution():
    """Calculate the number of apples bought by two men and three women at a certain store"""
    # Let x be the number of apples each woman bought
    # Then each man bought 30 apples and each woman bought x apples
    # Also, each man bought 20 less apples than each woman, so:
    # 30 = x - 20
    # x = 50

    # So each woman bought 50 apples
    # And the total number of apples bought by two men and three women is:
    total_apples = 2 * 30 + 3 * 50
    result = total_apples
    return result

print(solution())