def solution():
    """Kimberly went hiking and took a 4-liter bottle full of water with her. The first time she drank from it, she consumed a quarter of the water in the bottle. Later on, she drank 2/3rd of the remaining water. How much water is left in the bottle (in liters)?"""
    starting_amount = 4
    first_drink = starting_amount / 4
    remaining_amount = starting_amount - first_drink
    second_drink = remaining_amount * (2/3)
    final_amount = remaining_amount - second_drink
    result = final_amount
    return result

print(solution())