def solution():
    original_price = 50
    increase_percent = 30
    decrease_percent = 20

    # Calculate the new price after the 30% increase
    first_price = original_price + (original_price * increase_percent / 100)

    # Calculate the final price after the 20% decrease
    final_price = first_price - (first_price * decrease_percent / 100)
    result = final_price
    return result

print(solution())