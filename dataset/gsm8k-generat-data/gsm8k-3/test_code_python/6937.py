def solution():
    """The price of two kilograms of sugar and five kilograms of salt is $5.50. If a kilogram of sugar costs $1.50, then how much is the price of three kilograms of sugar and a kilogram of salt?"""
    # Define the price of sugar per kilogram
    SUGAR_PRICE = 1.50

    # Define the price of two kilograms of sugar and five kilograms of salt
    TWO_SUGAR_FIVE_SALT_PRICE = 5.50

    # Calculate the price of one kilogram of salt
    one_salt_price = (TWO_SUGAR_FIVE_SALT_PRICE - 2*SUGAR_PRICE) / 5

    # Calculate the price of three kilograms of sugar and one kilogram of salt
    three_sugar_one_salt_price = 3*SUGAR_PRICE + one_salt_price

    # Display the price of three kilograms of sugar and one kilogram of salt
    result = three_sugar_one_salt_price
    return result

print(solution())