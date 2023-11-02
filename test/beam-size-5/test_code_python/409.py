def solution():
    
    # Define the number of candles Marcy makes
    total_candles = 50000

    # Calculate the number of uncovered candles
    uncovered_candles = total_candles * 0.99

    # Calculate the number of uncovered candles
    uncovered_candles = total_candles - uncovered_candles

    # Calculate the number of smell candles
    smell_candles = uncovered_candles * 0.05

    # Display the number of smell candles
    result = smell_candles
    return result

print(solution())