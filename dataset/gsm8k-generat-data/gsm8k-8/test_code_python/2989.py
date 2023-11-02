def solution():
    # Define the conversion ratio between stamps and matches
    stamps_per_match = 1/12

    # Calculate the total number of matches Jimmy has
    jimmy_matches = 5 * 24

    # Convert Jimmy's matches to stamps
    jimmy_stamps = jimmy_matches * stamps_per_match

    # Calculate how many stamps Tonya has before the trade
    tonya_stamps_before_trade = 13

    # Subtract the stamps Tonya trades to Jimmy
    tonya_stamps_after_trade = tonya_stamps_before_trade - jimmy_stamps

    result = tonya_stamps_after_trade
    return result

print(solution())