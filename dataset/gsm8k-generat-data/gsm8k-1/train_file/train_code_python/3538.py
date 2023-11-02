def solution():
    """Peter and his dad Rupert shared the same birthday. To make it special, they each got their own birthday cake. Peter has 10 candles on his cake. Rupert is 3 and 1/2 times older than Peter. How many candles will be on Rupert's cake?"""
    peter_candles = 10
    rupert_age_ratio = 3.5
    rupert_candles = peter_candles * rupert_age_ratio
    result = rupert_candles
    return result

print(solution())