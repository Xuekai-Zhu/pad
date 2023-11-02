def solution():
    """Stephanie is decorating 24 cupcakes for a birthday party, but she needs more candles. She currently has a total of 30 candles. She wants to decorate half of the cupcakes with 1 candle each and the other half of the cupcakes with 2 candles each. How many additional candles does Stephanie need to complete the cupcakes?"""
    # Calculate the number of cupcakes that need 1 candle and 2 candles each
    cupcakes_with_1_candle = 12
    cupcakes_with_2_candles = 12

    # Calculate the number of candles needed for the cupcakes
    total_candles_needed = (cupcakes_with_1_candle * 1) + (cupcakes_with_2_candles * 2)

    # Calculate the number of additional candles needed
    additional_candles_needed = total_candles_needed - 30

    result = additional_candles_needed
    return result

print(solution())