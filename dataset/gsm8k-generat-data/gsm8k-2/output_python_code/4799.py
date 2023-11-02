def solution():
    """Aliyah has 10 more phones than her sister Vivienne. If Vivienne has 40 phones, and the two sisters sell their phones at $400 each, calculate the total amount of money they have together?"""
    vivienne_phones = 40
    aliyah_phones = vivienne_phones + 10
    phones_sold = vivienne_phones + aliyah_phones
    price_per_phone = 400
    total_money = phones_sold * price_per_phone
    result = total_money
    return result

print(solution())