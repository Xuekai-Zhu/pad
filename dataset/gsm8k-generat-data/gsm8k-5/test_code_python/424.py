def solution():
    initial_amount = 10000  # Rose had 10 kilograms of rice, so we convert to grams

    # Amount cooked in the morning
    morning_cooked = (9/10) * initial_amount

    # Amount remaining after morning cooking
    amount_remaining = initial_amount - morning_cooked

    # Amount cooked in the evening
    evening_cooked = (1/4) * amount_remaining

    # Total amount of rice left
    total_left = amount_remaining - evening_cooked

    result = total_left
    return result

print(solution())