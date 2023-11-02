def solution():
    """Aniyah has 6 times as many birthday candles as Ambika. If Ambika has four birthday candles, how many birthday candles will they have if they put the birthday candles together and shared them equally between themselves?"""
    # Define the number of candles Ambika has
    ambika_candles = 4

    # Calculate the number of candles Aniyah has
    aniyah_candles = ambika_candles * 6

    # Calculate the total number of candles
    total_candles = ambika_candles + aniyah_candles

    # Calculate the number of candles each person would get if they shared equally
    candles_per_person = total_candles / 2

    # Display the number of candles per person
    result = candles_per_person
    return result

print(solution())