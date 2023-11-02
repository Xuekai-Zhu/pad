def solution():
    """Jerry charges $20 to pierce someone's nose and 50% more to pierce their ears. If he pierces 6 noses and 9 ears, how much money does he make?"""
    # Define the price for nose piercing and the additional percentage for ear piercing
    NOSE_PRICE = 20
    EAR_PERCENTAGE = 0.5

    # Calculate the price for ear piercing
    EAR_PRICE = NOSE_PRICE * (1 + EAR_PERCENTAGE)

    # Calculate the total income from nose piercing
    nose_income = 6 * NOSE_PRICE

    # Calculate the total income from ear piercing
    ear_income = 9 * EAR_PRICE

    # Calculate the total income
    total_income = nose_income + ear_income

    # Display the total income
    result = total_income
    return result

print(solution())