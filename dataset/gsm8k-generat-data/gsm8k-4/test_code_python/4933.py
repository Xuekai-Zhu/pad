def solution():
    """Gloria has five times as many dimes as quarters in her graduation money. She decides to put 2/5 of the quarters aside for future use. If she has 350 dimes, calculate the combined number of quarters and dimes she has after putting aside 2/5 of the quarters?"""
    # Let's assume the number of quarters to be x
    # Then, the number of dimes will be 5*x
    # Total value of quarters = x * $0.25 = $0.25x
    # Total value of dimes = 5*x * $0.10 = $0.50x
    # Total value of all coins = $0.25x + $0.50x = $0.75x
    # Now, we know that the total number of dimes is 350, so
    # $0.50x = 350
    # x = 700 (number of quarters)
    # Gloria puts aside 2/5 of the quarters, which is (2/5)*700 = 280 quarters
    # She is left with 420 quarters and 350 dimes
    # Total value of quarters = 420 * $0.25 = $105
    # Total value of dimes = 350 * $0.10 = $35
    # Combined total = $105 + $35 = $140
    result = 140
    return result

print(solution())