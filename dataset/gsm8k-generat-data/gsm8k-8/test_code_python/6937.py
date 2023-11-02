def solution():
    # Define the given variables
    sugar_price = 1.5
    sugar_amount = 2
    salt_amount = 5
    total_price = 5.5

    # Calculate the price of 1 kilogram of salt
    salt_price = (total_price - (sugar_price * sugar_amount)) / salt_amount

    # Calculate the price of 3 kilograms of sugar and 1 kilogram of salt
    price = (sugar_price * 3) + salt_price

    result = price
    return result

print(solution())