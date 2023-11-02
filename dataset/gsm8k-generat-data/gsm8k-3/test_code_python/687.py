def solution():
    """Stephanie is decorating 24 cupcakes for a birthday party, but she needs more candles. She currently has a total of 30 candles. She wants to decorate half of the cupcakes with 1 candle each and the other half of the cupcakes with 2 candles each. How many additional candles does Stephanie need to complete the cupcakes?"""
    # Calculate the number of cupcakes that need 1 candle and the number that need 2 candles
    cupcakes_1 = 24 // 2  # floor division to get an integer
    cupcakes_2 = 24 - cupcakes_1

    # Calculate the total number of candles needed
    candles_needed = (cupcakes_1 * 1) + (cupcakes_2 * 2)

    # Calculate the number of additional candles needed
    additional_candles = candles_needed - 30

    # Display the number of additional candles needed
    result = additional_candles
    return result

print(solution())