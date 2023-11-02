def solution():
    # Define the number of candles Ambika has
    ambika_candles = 4

    # Calculate the number of candles Aniyah has
    aniyah_candles = 6 * ambika_candles

    # Calculate the total number of candles
    total_candles = ambika_candles + aniyah_candles

    # Calculate the number of candles each person gets after sharing equally
    candles_each = total_candles / 2

    # Round down to the nearest whole number of candles
    candles_each = int(candles_each)

    result = candles_each
    return result

print(solution())