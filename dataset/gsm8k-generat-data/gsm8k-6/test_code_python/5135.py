def solution():
    # Calculate the number of candles needed
    total_candles = 3 * Kerry_age  # Kerry wants his age in candles on each cake
    candles_per_box = 12  # candles come in boxes of 12
    cost_per_box = 2.5  # candles cost $2.5 per box
    cost_total = 5  # total cost of candles is $5

    # Calculate the Kerry's age
    Kerry_age = int(total_candles / candles_per_box) + 1  # round up to the nearest integer

    result = Kerry_age
    return result

print(solution())