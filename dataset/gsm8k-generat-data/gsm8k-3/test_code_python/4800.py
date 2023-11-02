def solution():
    """Aliyah has 10 more phones than her sister Vivienne. If Vivienne has 40 phones, and the two sisters sell their phones at $400 each, calculate the total amount of money they have together?"""
    # Define the price per phone
    PHONE_PRICE = 400

    # Define the number of phones Vivienne has
    vivienne_phones = 40

    # Calculate the number of phones Aliyah has
    aliyah_phones = vivienne_phones + 10

    # Calculate the total number of phones
    total_phones = vivienne_phones + aliyah_phones

    # Calculate the total amount of money they have together
    total_money = total_phones * PHONE_PRICE

    # Display the total amount of money
    result = total_money
    return result

print(solution())