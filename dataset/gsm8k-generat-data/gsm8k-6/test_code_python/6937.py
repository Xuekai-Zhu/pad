def solution():
    # Calculate the price of two kg of sugar and 5 kg of salt
    price_2kg_sugar_5kg_salt = 5.50

    # Calculate the price of one kg of sugar
    price_1kg_sugar = 1.50

    # Calculate the price of 3 kg of sugar
    price_3kg_sugar = 3 * price_1kg_sugar

    # Calculate the price of 1 kg of salt
    price_1kg_salt = (price_2kg_sugar_5kg_salt - (2 * price_1kg_sugar)) / 5

    # Calculate the price of 3 kg of sugar and 1 kg of salt
    price_3kg_sugar_1kg_salt = (3 * price_1kg_sugar) + price_1kg_salt

    result = price_3kg_sugar_1kg_salt
    return result

print(solution())