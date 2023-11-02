def solution():
    # Convert the milk and grape juice amounts to ounces
    milk_amount = 8
    grape_juice_amount = 16 * 2

    # Calculate the total amount of liquid consumed
    total_liquid = milk_amount + grape_juice_amount

    # Calculate the maximum amount of water Jamie can drink
    max_water_amount = 32 - total_liquid

    return max_water_amount

print(solution())