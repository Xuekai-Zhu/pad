def solution():
    vivienne_phones = 40
    aliyah_phones = vivienne_phones + 10
    phone_price = 400
    
    # Calculate the total number of phones the sisters have together
    total_phones = vivienne_phones + aliyah_phones
    
    # Calculate the total amount of money they earn from selling all their phones
    total_money = total_phones * phone_price
    result = total_money
    return result

print(solution())