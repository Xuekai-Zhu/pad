def solution():
    # Calculate the total number of candles bought
    total_candles = 5 / 2.5  # $5 spent on candles, and each box costs $2.5

    # Calculate the total number of candles needed for three cakes
    candles_per_cake = 1  # Kerry wants his age in candles on each cake
    total_candles_needed = candles_per_cake * 3 * Kerry_age

    # Calculate Kerry's age by dividing the total number of candles needed by 12 (number of candles in a box)
    Kerry_age = total_candles_needed / 12
    result = Kerry_age
    return result

print(solution())