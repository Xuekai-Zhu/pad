def solution():
    closing_price = 8722
    percent_change = 0.02 # 2% decrease

    # Calculate the original price before the decrease
    original_price = closing_price / (1 - percent_change)

    result = original_price
    return result

print(solution())