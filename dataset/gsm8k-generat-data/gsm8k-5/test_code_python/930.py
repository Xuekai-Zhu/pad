def solution():
    # Let's call the number of apples each woman bought "x"
    # Then each man bought 30 apples and each woman bought x apples

    # The total number of apples bought by the women is 3x
    total_apples_women = 3 * x

    # Each woman bought 20 more apples than each man
    # So x = 30 + 20 = 50
    x = 50

    # Total number of apples bought by everyone
    total_apples = 2 * 30 + total_apples_women

    result = total_apples
    return result

print(solution())