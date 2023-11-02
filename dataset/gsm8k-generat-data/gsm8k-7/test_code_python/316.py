def solution():
    original_price = 220
    increase_percent = 0.15  # 15% increase

    # Calculate the amount of the increase
    increase_amount = original_price * increase_percent

    # Calculate the new price
    new_price = original_price + increase_amount
    result = new_price
    return result

print(solution())