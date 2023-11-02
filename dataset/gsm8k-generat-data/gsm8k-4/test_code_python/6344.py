def solution():
    """Daniel has 5 jars of juice containing 2 liters each. He wants to serve a full glass of juice to each person at a party. He knows that each glass can hold up to 250 milliliters of juice. How many full glasses can he give?"""
    # Define the total amount of juice in liters
    total_juice_liters = 5 * 2

    # Convert the total amount of juice to milliliters
    total_juice_milliliters = total_juice_liters * 1000

    # Calculate the number of full glasses of juice he can serve
    full_glasses = total_juice_milliliters // 250

    # Return the result
    result = full_glasses
    return result

print(solution())