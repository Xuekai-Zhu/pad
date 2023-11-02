def solution():
    vivienne_phones = 40  # Vivienne has 40 phones
    aliyah_phones = vivienne_phones + 10  # Aliyah has 10 more phones than Vivienne
    phone_price = 400  # They sell each phone at $400

    # Calculate the total amount of money they make from selling their phones
    total_amount = (vivienne_phones + aliyah_phones) * phone_price
    result = total_amount
    return result

print(solution())