def solution():
    """Peter and his dad Rupert shared the same birthday. To make it special, they each got their own birthday cake. Peter has 10 candles on his cake. Rupert is 3 and 1/2 times older than Peter. How many candles will be on Rupert's cake?"""
    # Define the number of candles on Peter's cake
    peter_candles = 10

    # Calculate the age ratio between Peter and Rupert
    age_ratio = 3.5

    # Calculate the number of candles on Rupert's cake
    rupert_candles = round(peter_candles * age_ratio)

    result = rupert_candles
    return result

print(solution())