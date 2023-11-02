def solution():
    original_price = 220  # The selling price of the bicycle last year
    increase_percent = 15  # The percentage increase in price

    # Calculate the new price after the increase
    new_price = original_price + (original_price * (increase_percent / 100))

    result = new_price
    return result

print(solution())