def solution():
    # Calculate the original amount Mathilda owed
    remaining_amount = 0.75  # 75% left to pay
    original_amount = (125 / (1 - remaining_amount))  # using formula to calculate original amount
    result = original_amount
    return result

print(solution())