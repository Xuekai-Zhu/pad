def solution():
    ambika_candles = 4  # Ambika has 4 birthday candles
    aniyah_candles = 6 * ambika_candles  # Aniyah has 6 times as many candles as Ambika

    # Calculate the total number of candles they will have if they combine them
    total_candles = ambika_candles + aniyah_candles

    # Calculate how many candles each person will get if they divide them equally
    candles_per_person = total_candles / 2
    result = candles_per_person
    return result

print(solution())