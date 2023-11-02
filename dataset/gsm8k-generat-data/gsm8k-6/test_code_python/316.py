def solution():
    original_price = 220  # selling price of the bicycle last year
    percentage_increase = 15  # increase in percentage
    new_price = original_price + (original_price * percentage_increase / 100)  # calculate the new price
    result = new_price
    return result

print(solution())