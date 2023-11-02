def solution():
    """Aliyah has 10 more phones than her sister Vivienne. If Vivienne has 40 phones, and the two sisters sell their phones at $400 each, calculate the total amount of money they have together?"""
    # Define the number of phones each sister has
    vivienne_phones = 40
    aliyah_phones = vivienne_phones + 10

    # Calculate the total number of phones they have together
    total_phones = vivienne_phones + aliyah_phones

    # Calculate the total amount they can get from selling their phones
    total_amount = total_phones * 400

    # return the result
    result = total_amount
    return result

print(solution())