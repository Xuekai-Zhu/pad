def solution():
    """Miley bought two cellphones for her parents. Each cellphone costs $800 but, since she is buying two units, she will receive a 5% discount for the total cost. How much did Miley pay?"""
    phone_cost = 800
    num_phones = 2
    discount_percent = 5
    total_cost = phone_cost * num_phones
    discount_amount = (discount_percent / 100) * total_cost
    total_cost -= discount_amount
    result = total_cost
    return result

print(solution())