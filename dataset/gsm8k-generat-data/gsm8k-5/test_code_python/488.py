def solution():
    original_price = 500  # Mrs. Smith planned to spend $500
    additional_percent = 2/5  # She needed 2/5 more money than she had
    total_price = original_price * (1 + additional_percent)  # Calculate the total price of her items
    discounted_price = total_price * 0.85  # Calculate the discounted price
    remaining_money = discounted_price - original_price  # Calculate how much more money Mrs. Smith will still need
    result = remaining_money
    return result

print(solution())