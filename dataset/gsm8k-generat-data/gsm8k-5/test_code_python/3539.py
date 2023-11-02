def solution():
    peter_candles = 10  # Peter has 10 candles on his cake
    rupert_age_ratio = 3.5  # Rupert is 3 and 1/2 times older than Peter

    # Calculate Peter's age based on the number of candles on his cake
    peter_age = peter_candles + 1  # Assume Peter has one candle for each year plus an extra one for good luck

    # Calculate Rupert's age based on the ratio of his age to Peter's age
    rupert_age = rupert_age_ratio * peter_age

    # Calculate the number of candles on Rupert's cake based on his age
    rupert_candles = rupert_age + 1  # Assume Rupert has one candle for each year plus an extra one for good luck

    result = rupert_candles
    return result

print(solution())