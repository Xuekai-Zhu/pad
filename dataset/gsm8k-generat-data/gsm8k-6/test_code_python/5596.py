def solution():
    # Calculate the current number of whales in the sea
    current_whales = 2 * 4000  # double the number of whales from last year
    # Add the predicted increase in whales next year
    total_whales_next_year = current_whales + 800
    result = total_whales_next_year
    return result

print(solution())