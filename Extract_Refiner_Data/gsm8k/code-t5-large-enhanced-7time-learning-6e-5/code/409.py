def solution():
    
    total_candles = 50000
    non_expensive_candles = total_candles * 0.99
    defect_candles = non_expensive_candles * 0.05
    wet_dog_expensive_candles = non_expensive_candles - defect_candles
    both_expensive_and_expensive_candles = wet_dog_expensive_candles
    result = both_expensive_and_expensive_candles
    return result

print(solution())